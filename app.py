import streamlit as st
from PIL import Image
from utils import rooftop_analysis, solar_calculator, ai_insights, solar_data
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Industry AI Assistant", layout="wide")

# Title and subtitle
st.title("🌞 Solar Industry AI Assistant")
st.markdown(
    "<h4 style='color:#2E8B57;'>Estimate rooftop solar potential, costs, and ROI with easy inputs and AI insights</h4>",
    unsafe_allow_html=True,
)
st.write("---")

# How to Use section with sidebar details / instructions
with st.expander("ℹ️ How to Use - Step by Step", expanded=True):
    st.markdown(
        """
        ### Step 1: Upload your rooftop image  
        Use a clear aerial or satellite photo of your rooftop.

        ### Step 2: Customize inputs in the sidebar  
        - **Latitude & Longitude:** Enter rooftop location for accurate solar data.  
        - **Electricity Cost ($/kWh):** Your electricity tariff for savings calculation.  
        - **System Cost ($/Watt):** Installation cost estimate per watt.

        Adjust these anytime to see updated results!

        ### Step 3: View detailed outputs  
        - Rooftop mask segmentation highlighting solar-suitable areas.  
        - Estimated rooftop area (m²).  
        - Annual solar energy estimate (kWh).  
        - Installation cost and annual savings.  
        - ROI payback period with AI recommendations.

        ### Step 4: Download comprehensive project report.
        """
    )

# Sidebar Inputs with tooltips
st.sidebar.title("⚙️ Customize Inputs")
st.sidebar.markdown("Enter rooftop location and cost parameters:")

latitude = st.sidebar.number_input(
    "Latitude", value=37.7749, format="%.6f",
    help="Rooftop latitude (e.g., 37.7749)"
)
longitude = st.sidebar.number_input(
    "Longitude", value=-122.4194, format="%.6f",
    help="Rooftop longitude (e.g., -122.4194)"
)
electricity_cost = st.sidebar.number_input(
    "Electricity Cost ($/kWh)", value=0.20, step=0.01,
    help="Your electricity price per kWh"
)
system_cost = st.sidebar.number_input(
    "System Cost ($/Watt)", value=2.5, step=0.1,
    help="Estimated installation cost per watt"
)

uploaded_file = st.file_uploader(
    "📷 Upload Rooftop Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"]
)

def calculate_financials(irradiance_per_kwp, electricity_cost, system_cost, roof_area_m2, panel_efficiency=0.18):
    installed_kwp = roof_area_m2 * panel_efficiency
    total_cost = installed_kwp * 1000 * system_cost   # watts * cost per watt
    annual_energy = irradiance_per_kwp * installed_kwp
    annual_savings = annual_energy * electricity_cost
    payback_years = total_cost / annual_savings if annual_savings > 0 else float('inf')
    return total_cost, annual_savings, payback_years

def generate_professional_ai_recommendations(rooftop_area, annual_energy, installation_cost, roi_payback):
    return f"""
Given your rooftop solar data — Rooftop Area: {rooftop_area:.2f} m², Annual Solar Energy: {annual_energy:.2f} kWh, Installation Cost: ${installation_cost:,.2f}, ROI Payback: {roi_payback:.1f} years — here are practical recommendations:

Solar Installation Recommendations:  
- Structural Assessment: Confirm rooftop strength and minimal shading.  
- High-Quality Components: Use panels with 18–22% efficiency and trusted inverters.  
- Optimal Positioning: Tilt and orient panels based on your latitude.  
- Compliance: Use certified installers to meet codes and permits.

Maintenance Best Practices:  
- Regular Cleaning: Clean every 1–3 months with gentle water sprays.  
- Periodic Inspections: Monthly checks for shading, dirt, damage, wiring issues.  
- Vegetation Management: Trim trees and plants to prevent shading losses.  
- Performance Monitoring: Track output via inverter dashboards and monitoring apps.  
- Annual Professional Checks: Schedule yearly technical inspections.

Financial & Utility Considerations:  
- Incentives & Net Metering: Leverage local programs and subsidies.  
- Electricity Tariff Awareness: Review rates regularly to optimize savings.  
- Warranties & Service Contracts: Maintain coverage for reliability and uptime.
"""

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Rooftop Image", use_container_width=True)

    rooftop_mask, roof_area_m2 = rooftop_analysis.extract_rooftop(image)

    col1, col2 = st.columns(2)
    with col1:
        st.header("🏠 Rooftop Mask")
        st.image(rooftop_mask, use_container_width=True)
    with col2:
        st.header("Rooftop Area (m²)")
        st.metric(label="Area", value=f"{roof_area_m2:.2f} m²")

    irradiance_per_kwp = solar_data.get_pvgis_irradiance(latitude, longitude)

    if irradiance_per_kwp is None:
        st.error("⚠️ Solar irradiation data not available for this location.")
    else:
        total_cost, annual_savings, payback_years = calculate_financials(
            irradiance_per_kwp, electricity_cost, system_cost, roof_area_m2)

        estimated_annual_energy = irradiance_per_kwp * roof_area_m2 * 0.18  # energy using panel efficiency

        st.header("⚡ Solar Potential & Financial Summary")
        st.write(f"**Estimated Annual Solar Energy:** {estimated_annual_energy:.2f} kWh")
        st.write(f"**Estimated Installation Cost:** ${total_cost:,.2f}")
        st.write(f"**Estimated Annual Savings:** ${annual_savings:,.2f}")
        st.write(f"**ROI Payback Period:** {payback_years:.1f} years")

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(["Payback (years)"], [payback_years], color="#2E8B57")
        ax.set_ylim(0, max(15, payback_years + 5))
        st.pyplot(fig)

        ai_output = generate_professional_ai_recommendations(
            roof_area_m2,
            estimated_annual_energy,
            total_cost,
            payback_years
        )

        st.header("🤖 AI Recommendations")
        st.write(ai_output)

        report = f"""
Solar Industry AI Assistant Report
-----------------------------------
Location: {latitude}, {longitude}
Rooftop Area: {roof_area_m2:.2f} m²
System Size: {roof_area_m2 * 0.18:.2f} kWp
Annual Solar Energy: {estimated_annual_energy:.2f} kWh
Installation Cost: ${total_cost:,.2f}
Annual Savings: ${annual_savings:,.2f}
ROI Payback Period: {payback_years:.1f} years

AI Recommendations:
{ai_output}
"""
        st.download_button("📥 Download Full Report", report, "solar_report.txt", "text/plain")
else:
    st.info("Please upload a rooftop image to start your analysis.")
