import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_URL_PRIMARY = os.getenv("HF_API_URL_PRIMARY")
HF_API_URL_FALLBACK = os.getenv("HF_API_URL_FALLBACK")
HF_API_KEY = os.getenv("HF_API_KEY")

HF_API_URLS = [HF_API_URL_PRIMARY, HF_API_URL_FALLBACK]

def get_ai_recommendations(rooftop_data):
    if not HF_API_KEY:
        raise Exception("Missing HF_API_KEY environment variable.")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        f"Given the rooftop solar metrics below, provide detailed installation recommendations, "
        f"financial outlook including ROI, and maintenance tips in clear text:\n\n"
        f"Detected Area (m2): {rooftop_data['detected_area_m2']}\n"
        f"Usable Ratio: {rooftop_data['usable_ratio']}\n"
        f"Orientation: {rooftop_data['orientation']}\n"
        f"Shading Factor: {rooftop_data['shading_factor']}\n"
        f"Annual Generation (kWh): {rooftop_data['solar_metrics']['annual_generation_kWh']}\n"
        f"System Cost (INR): {rooftop_data['solar_metrics']['system_cost_inr']}\n"
        f"Annual Savings (INR): {rooftop_data['solar_metrics']['annual_savings_inr']}\n"
        f"ROI Years: {rooftop_data['solar_metrics']['roi_years']}\n"
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.5
        }
    }

    last_error = None
    for url in HF_API_URLS:
        if not url:
            continue
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and 'generated_text' in result[0]:
                    return result[0]['generated_text']
                elif isinstance(result, dict) and 'generated_text' in result:
                    return result['generated_text']
                else:
                    return str(result)
            else:
                last_error = Exception(f"Error {response.status_code}: {response.text} from {url}")
        except Exception as e:
            last_error = e
    raise last_error or Exception("All API URLs failed.")
