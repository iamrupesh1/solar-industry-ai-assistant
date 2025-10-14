# 🌞 Solar Industry AI Assistant  

[![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)](https://streamlit.io/) 
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/) 
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-AI-orange)](https://huggingface.co/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 🧭 Overview

**Solar Industry AI Assistant** is an advanced AI-powered web application designed to revolutionize how homeowners and solar professionals evaluate rooftop solar potential using satellite imagery.  

It combines **computer vision**, **financial modeling**, and **LLM-based recommendations** to deliver end-to-end solar analysis — from rooftop area detection to ROI estimation — all within an interactive Streamlit interface.

## Project Goal
- Analyze rooftops from satellite images.
- Provide accurate solar potential assessments.
- Generate installation and maintenance recommendations.
- Calculate installation cost, energy savings, and ROI payback period.

## ⚡ Key Features

- 🔍 **Automated Rooftop Segmentation**  
  Vision AI detects and maps solar-suitable rooftop areas from satellite imagery.
- ☀️ **Solar Potential Estimation**  
  Calculates annual energy generation (kWh/year) using rooftop geometry and local irradiance data.
- 💰 **Financial Insights & ROI Calculation**  
  Provides cost breakdowns, expected annual savings, and payback period estimates.
- 🤖 **AI-Driven Recommendations**  
  LLMs generate professional installation, maintenance, and efficiency improvement suggestions.
- 🖥️ **Interactive Streamlit Interface**  
  User-friendly dashboard for image upload, visual analysis, and detailed reports.
- ☁️ **Cloud Deployment (Live Demo)**  
  Hosted on Streamlit Cloud for fast, global access.

---

## 🎥 Demo & Live Link

👉 **Live App:** [Solar Industry AI Assistant](https://solar-industry-ai-assistant-gtwcsappsboh3kzjpphfzyw.streamlit.app/)

---

## 🧠 Technologies & Skills

### **Core Technologies**
- **Programming:** Python 3.9+  
- **Framework:** Streamlit  
- **AI/ML:** Vision AI (rooftop segmentation), Hugging Face LLMs  
- **Data Integration:** PVGIS solar irradiance API & satellite imagery  
- **Deployment:** Streamlit Cloud  
- **Version Control:** Git & GitHub  

### **Skills Demonstrated**
- 🧩 Computer Vision for Satellite Image Analysis  
- 💬 Prompt Engineering & Context-Aware AI Responses  
- 📊 Financial Modeling (Installation Cost, ROI Analysis)  
- 🧱 Modular & Documented Python Code  
- ☁️ Cloud App Deployment & API Integration  
- ⚙️ Error Handling, Data Validation & Output Structuring  


## Future Work

- Integrate end-to-end AI rooftop segmentation models  
- Add localized subsidy and incentive support  
- Multi-language AI recommendations  
- Cloud-based scaling and API backend support  
- Long-term system performance monitoring and forecasting

 ## 👨‍💻 Author

**Rupesh Kumar Shah**  

📧 **Email:** [shahrupesh511@gmail.com](mailto:shahrupesh511@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/rupesh-kumar-shah-691458292](https://www.linkedin.com/in/rupesh-kumar-shah-691458292/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BUfqdpUvNRoSDoX9ztvpIzg%3D%3D)  
💻 **GitHub:** [iamrupesh1](https://github.com/iamrupesh1)




## 🙏 Acknowledgment

Thank you for exploring the **Solar Industry AI Assistant** project!  
This work reflects my passion and growing expertise in **Artificial Intelligence** and **Renewable Energy Innovation** — combining technology and sustainability to create real-world impact.


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

