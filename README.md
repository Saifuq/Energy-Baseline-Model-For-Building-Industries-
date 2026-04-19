# ⚡ Energy Baseline Model for Building and Industries
### Premier AI-Driven Energy Orchestration & Industrial Baseline Reporting for India

[![Live Application](https://img.shields.io/badge/Live_Dashboard-Launch_Streamlit-F97316?style=for-the-badge&logo=streamlit)](https://energy-baseline-model-for-building-industries.streamlit.app/)

> **Supervisor:** Dr. Sivasankari Sundaram  
> **Creator & Researcher:** Saifuddin Farooqui (BTP Research Division)

---

## 🌐 Live Web Application
Experience the model live in your browser! The Streamlit interface was chosen specifically because it offers unparalleled dynamic rendering—allowing real-time interaction with 16 local Indian cities, diverse building configurations, and instantaneous financial/carbon benchmarking without a single line of code.

👉 **[Access the Live AI Dashboard Here](https://energy-baseline-model-for-building-industries.streamlit.app/)** 

---

## 🎯 Project Objective
The central objective of this BTP project is to architect a highly robust, scalable **Energy Baseline AI Engine** capable of calculating the zero-point thermal and mechanical loads of commercial buildings. By predicting the natural energy demand, we empower facility managers, auditors, and stakeholders to execute cost-effective retrofits, cut operational expenses (OPEX), and verify carbon offsets in direct alignment with India's "Panchamrit" Net Zero 2070 climate goals.

---

## 🚧 Challenges Faced: The Indian Context Data Gap
One of the most persistent hurdles in Southeast Asian energy modeling is the extreme scarcity of high-fidelity, public-domain sub-metered energy datasets specific to Indian climate zones and infrastructure standards.

**Our AI Solution:**
Instead of relying on heuristic averages, we successfully engineered a cross-pollination methodology. We utilized the extensive global thermophysical interactions natively trapped within the **2.5+ Million row ASHRAE Great Energy Predictor corpus**, and localized that intelligence by ingesting real-time celestial and barometric metrics via the **NASA POWER API** combined with synthetic IMD (Indian Meteorological Department) profiles.

---

## 🧠 Modeling Algorithm & Code Overview
This project relies on **XGBoost (Extreme Gradient Boosting)**—specifically the historiated tree variance (hist)—as the core algorithmic workhorse. 

- **Why XGBoost?** Traditional linear regressions fail to model the non-linear interplay between solar radiation, shifting humidity, occupational hours, and mechanical efficiencies. XGBoost leverages parallel tree boosting to efficiently capture these multi-dimensional splits.
- **Code Workflow:**
  1. `energy_baseline_model.py`: Ingests the 2.5M raw records, executes strict feature engineering, handles categorical mapping, trains the XGBoost trees, and serializes the state to `xgboost_india_model.json`. Simultaneously queries NASA POWER for district weather caching.
  2. `app.py`: The live ecosystem. It dynamically deserializes the model payload, intercepts user GUI tweaks (What-If logic), applies Streamlit's reactive loop rendering, and returns Plotly-based insights.

---

## ⚙️ Key Parameters
The model tracks and evaluates over 31 discrete features. The most critical operational levers available to the user include:
- **Built-up Area (Sq.Ft)** and **Building Age**: The baseline volumetric identifiers.
- **HVAC COP (Coefficient of Performance)**: The foundational mechanical cooling efficiency scale.
- **Envelope ACH (Air Changes/Hour)**: Represents facility leakage and sealing integrity.
- **Glass SHGC (Solar Heat Gain Coefficient)**: Translates local solar irradiation into internal HVAC thermal load.
- **Electricity Tariff (₹/kWh)**: Converts pure physics into executive-level financial ROI algorithms.

---

## 📈 Outstanding Results & Deliverables
The engine performs at **Gold Standard** metrics, generating predictive forecasts that comfortably satisfy stringent ASHRAE Guideline 14 standards. Fast computation allows the architecture to visualize three layers of reporting instantly:
1. **Financial Efficacy**: Waterfall ROI tracking predicting **10-30% OPEX savings**.
2. **Regulatory Compliance**: Instant evaluation against ECBC 2017/2024 baselines.
3. **Carbon Reporting**: Pinpoint CO₂ avoidance measured in localized metric tonnage footprinting.

---

## 📊 Technology Stack
- **AI / ML Engine**: Python 3.9+, XGBoost, Scikit-Learn
- **Data Engineering**: Pandas, NumPy
- **Interactive Frontend**: Streamlit (Advanced Glassmorphism UI/UX)
- **Mathematical Visualization**: Plotly, Matplotlib, SHAP (Explainable AI module)
- **External Dependencies**: NASA POWER API

---

## 🚀 Installation & Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saifuddin-farooqui/BTP-Energy-Engine.git
   cd BTP-Energy-Engine
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

* Thank You! 
