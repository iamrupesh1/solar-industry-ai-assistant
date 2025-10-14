def calc_financials(annual_kwh, elec_cost_per_kwh, system_cost_per_watt, installed_kwp):
    # Calculate installation cost
    total_cost = installed_kwp * 1000 * system_cost_per_watt  # watts to watts * cost per watt

    # Calculate annual savings
    annual_savings = annual_kwh * elec_cost_per_kwh

    # Calculate payback period safely
    if annual_savings == 0:
        payback_years = float('inf')
    else:
        payback_years = total_cost / annual_savings

    return total_cost, annual_savings, payback_years
