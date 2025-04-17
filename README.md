# 🦟 Trendemic: Forecasting Dengue Fever Outbreaks with Machine Learning

**Trendemic** is an advanced forecasting platform using machine learning and time series modeling to **predict dengue outbreaks** in **San Juan (Puerto Rico)**, **Iquitos (Peru)**, and across **both cities** via an ensemble-based meta model.

Our goal? Move from reactive crisis response to **data-driven epidemic prevention.**

---

## 🌍 Why It Matters

Dengue fever, transmitted by the *Aedes aegypti* mosquito, is exploding in prevalence — driven by climate change, urbanization, and inadequate infrastructure.

- 🏝️ *San Juan*: 21,000+ cases in 2010, avg. cost $38.7M/year
- 🌴 *Iquitos*: 24,000+ cases in 2011, $4.5M/year in costs

---

## 🧠 Modeling Strategy

We modeled dengue outbreaks across **three levels**:

### 🧩 1. City-Specific Models

Each city has unique seasonality, outbreak frequency, and environmental predictors.

#### **San Juan (SJ)**
- Best classical model: `SARIMA(1,1,1)(0,1,1,52)` + log transform  
  **MAE:** 17.38  
- XGBoost ensemble: **MAE: 7.21**

#### **Iquitos (IQ)**
- Best SARIMA: `SARIMA(2,1,2)(1,1,1,52)`  
  **MAE:** ~15.12 (±)  
- Log-transformed SARIMA + exogenous variables improved stability  
- XGBoost again **outperformed SARIMA** with **MAE: 8.14**

---

### 🧬 2. Combined City Meta-Model

To leverage cross-city generalizability, we trained a **combined ensemble model** using both cities' features.

> **Best Overall MAE: 6.15** ✅  
> Significantly better generalization across testing datasets than any single-city model.

Techniques:
- Blended SARIMA and XGBoost predictions
- Feature engineering to include city identifier, lag effects, and temporal encodings
- Meta-regressor to minimize residual error from individual models

---

### 📈 Ensemble Techniques

- **SARIMA/SARIMAX** for seasonality, trends
- **Log transforms** to stabilize variance
- **XGBoost** for peak detection and non-linear interactions
- **Rolling forecasts** + AIC/BIC/Ljung-Box diagnostics
- **Meta-ensemble** for final predictions (stacked)

---

## 📊 Forecasting Results

| Model Type                   | Target City     | MAE    | Notes                                      |
|-----------------------------|------------------|--------|--------------------------------------------|
| SARIMA (log)                | San Juan         | 17.38  | Strong seasonal capture                    |
| SARIMAX (log + exog)        | San Juan         | 17.54  | Slightly worse with climate features       |
| XGBoost                     | San Juan         | 7.21   | Best SJ-specific model                     |
| SARIMA                      | Iquitos          | ~15.12 | Required deeper seasonal tuning            |
| XGBoost                     | Iquitos          | 8.14   | Best IQ-specific model                     |
| Combined City Ensemble      | SJ + IQ          |**6.15**| Best overall — generalized learning🏆      |

---

## 📁 Repo Structure

```bash
📦 trendemic
├── notebooks/
│   ├── ensemble_model.ipynb
│   ├── ARIMA_analysis.ipynb
│   └── combined_city_model.ipynb
├── data/
│   ├── dengue_train_engineered.csv
│   └── dengue_test_engineered.csv
├── models/
│   └── saved_models/
├── README.md
└── requirements.txt
