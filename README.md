# 🌞 Solar Industry AI Assistant  

[![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)](https://streamlit.io/) 
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/) 
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-AI-orange)](https://huggingface.co/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---
## 🎥 Demo & Live Link

👉 **Live App:** [Solar Industry AI Assistant](https://solar-industry-ai-assistant-gtwcsappsboh3kzjpphfzyw.streamlit.app/)





## 🧭 Overview

**Solar Industry AI Assistant** is an **AI-powered web application** designed to help homeowners and solar professionals **evaluate rooftop solar potential** using **satellite imagery**.  

It combines computer vision, solar irradiance data modeling, and AI-driven recommendations to deliver an intelligent end-to-end solar potential analysis — from rooftop detection to ROI estimation — all within an interactive Streamlit interface..

## Project Goal
- Analyze rooftops from satellite images.
- Provide accurate solar potential assessments.
- Generate installation and maintenance recommendations.
- Calculate installation cost, energy savings, and ROI payback period.

## ⚙️ System Workflow
    
 1. **Upload rooftop image**  
       Upload a clear satellite or aerial rooftop photo.
 2. **Enter location & cost parameters (Sidebar/optional)**  
       - Latitude and Longitude → fetch solar irradiance data  
       - Electricity Cost ($/kWh) → for energy savings estimation  
       - System Cost ($/Watt) → for installation cost calculation
 3. **Image processing (OpenCV)**  
       Extracts the rooftop area and highlights solar-suitable regions.
 4. **Fetch solar irradiance data (PVGIS API)**  
       Retrieves location-based annual solar energy data automatically.
 5. **Financial modeling**  
       Computes energy generation, installation cost, savings, and ROI payback period.
 6. **AI-driven recommendations**  
       Provides practical installation and maintenance suggestions (locally simulated).
 7. **Results and report generation**  
       Displays rooftop mask, energy summary, payback chart, and allows report download.
 


## ⚡ Key Features

- 🔍 **Automated Rooftop Segmentation**  
 Uses OpenCV-based image processing to estimate rooftop area from uploaded satellite images.
- ☀️ **Solar Potential Estimation**  
  Calculates annual energy generation (kWh/year) using rooftop geometry and local irradiance data.
- 💰 **Financial Insights & ROI Calculation**  
  Provides cost breakdowns, expected annual savings, and payback period estimates.
- 🤖 **AI-Driven Recommendations**  
 Provides expert-style installation and maintenance tips powered by AI logic (currently locally simulated, with optional Hugging Face LLM integration).
- 🖥️ **Interactive Streamlit Interface**  
  User-friendly dashboard for image upload, visual analysis, and detailed reports.
- ☁️ **Cloud Deployment (Live Demo)**  
  Hosted on Streamlit Cloud for fast, global access.

---
## 🧠 Technologies & Skills

### **Core Technologies**
- **Programming:** Python 3.9+  
- **Framework:** Streamlit  
- **AI/ML:** OpenCV-based rooftop detection, PVGIS data modeling, optional Hugging Face integration
- **Data Integration:** PVGIS solar irradiance API & satellite imagery  
- **Deployment:** Streamlit Cloud  
- **Version Control:** Git & GitHub  

### **Skills Demonstrated**
- 🧩 **Computer Vision & Image Processing** — Applied OpenCV for rooftop segmentation and solar-suitable area detection.  
- ☀️ **Data Integration & API Handling** — Integrated **real-time solar irradiance data** from the **PVGIS API**.  
- 📊 **Financial & ROI Modeling** — Calculated installation cost, energy output, and payback period.  
- 💬 **Prompt Engineering & AI Logic Simulation** — Designed AI-driven installation & maintenance recommendations (ready for LLM integration).  
- 🧱 **Modular, Documented, and Scalable Python Codebase** — Followed clean architecture principles with reusable components.  
- ⚙️ **Robust Error Handling & Data Validation** — Ensured smooth user experience through structured exception handling and safe input validation.  
- ☁️ **Cloud Deployment & Version Control** — Deployed app on Streamlit Cloud and managed source code via Git & GitHub.


## Future Work

- Integrate deep learning-based rooftop segmentation (e.g., SAM or U-Net)
- Enable live LLM recommendations via Hugging Face API
- Add regional subsidy, incentive, and tariff support
- Implement multilingual interface for global users
- Develop real-time monitoring dashboard



## 👨‍💻 Author

**Rupesh Kumar Shah**  

📧 **Email:** [shahrupesh511@gmail.com](mailto:shahrupesh511@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/rupesh-kumar-shah-691458292](https://www.linkedin.com/in/rupesh-kumar-shah-691458292/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BUfqdpUvNRoSDoX9ztvpIzg%3D%3D)  
💻 **GitHub:** [iamrupesh1](https://github.com/iamrupesh1)




## 🙏 Acknowledgment

Thank you for exploring the **Solar Industry AI Assistant** project!  This project reflects my **passion for Artificial Intelligence** and **Renewable Energy Innovation**, combining technology and sustainability to create **real-world impact**.


## 🚀 Run Locally
  
### **Prerequisites**
- Python 3.9+  
- `.env` file containing your Hugging Face API token  

### **Installation**

```bash
# Clone the repository
git clone https://github.com/iamrupesh1/solar-industry-ai-assistant.git

# Navigate to the project directory
cd solar-industry-ai-assistant

# Install dependencies
pip install -r requirements.txt

# Run the app locally
streamlit run app.py

