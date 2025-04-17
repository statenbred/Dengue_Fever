# 🦟 Trendemic: Forecasting Dengue Fever Outbreaks with Machine Learning

**Trendemic** is an advanced forecasting platform that users machine learning and time series modeling to **predict dengue outbreaks**. For this project, I looked at two cities in **San Juan (Puerto Rico)**, **Iquitos (Peru)**.

The goal for this project was to create a predictor model that can take us from reactive crisis response to **data-driven epidemic prevention.**

---

## 🌍 Why It Matters

Dengue fever, transmitted by the *Aedes aegypti* mosquito, is exploding in prevalence — driven by climate change, urbanization, and inadequate infrastructure. Dengue is most common in tropical and subtropical areas, but it's also becoming a concern in urbanized communities. The majority of annual costs to combat dengue fever fall on local governments, and the homes and families of those effected by dengue fever.

- 🏝️ *San Juan*: 21,000+ cases in 2010, avg. cost $38.7M/year
- 🌴 *Iquitos*: 24,000+ cases in 2011, $4.5M/year in costs

---

## 🔧 Feature Engineering Pipeline

I implemented an advanced time-series-aware feature engineering strategy to maximize model performance:

- **Lagged Target Variables**
  - `total_cases_lag1`, `lag2`, etc., capturing temporal momentum
- **Rolling Statistics**
  - Rolling means and standard deviations over multiple windows (4, 8, 13, 26, and 52 weeks)
- **Climatological Signals**
  - `reanalysis_specific_humidity_g_per_kg`
  - `reanalysis_relative_humidity_percent`
  - `reanalysis_tdtr_k` (temperature range)
  - `precipitation_amt_mm`
  - `ndvi_ne`, `ndvi_nw`, `ndvi_sw`, etc. (vegetation indices)
- **Smoothed Aggregates**
  - `roll_mean`, `roll_std`, and multi-week trendlines

> All the features were engineered with **no target leakage**, using only prior data to simulate real-time forecasting conditions.

---

## 🧠 Modeling Strategy

I modeled dengue outbreaks across **three levels**:

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

I trained a **combined ensemble model** using both cities' features to leverage cross-city generalizability.

> **Best Overall MAE: 6.15** ✅  
> Significantly better generalization across testing datasets than any single-city model (including the LSTM model).

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

## 🤖 Deep Learning with LSTM

To push performance further, we developed an **LSTM (Long Short-Term Memory)** neural network using TensorFlow/Keras. This architecture excels at modeling long-term dependencies and temporal lags in sequential data.

### 🧱 Model Architecture
- **Input**: Sliding window of time steps (case counts + engineered features)
- **Layers**:
  - `LSTM(64)` → `Dropout(0.2)`
  - `Dense(32)` → `ReLU`
  - `Dense(1)` → Output
- **Optimizer**: Adam
- **Loss Function**: MSE
- **Training Window (lookback)**: 12–26 weeks

### 📉 Performance

| City     | LSTM MAE | Notes |
|----------|----------|-------|
| San Juan | **6.89** | Lower error than SARIMA/XGBoost |
| Iquitos  | **7.41** | Better at outbreak transitions  |

Key strengths of the LSTM model:
- Captured **nonlinear, delayed climate signals**
- Learned **seasonal recurrence** across years
- Smoothed forecasts during periods of volatility

> The LSTM performed comparably to the combined city ensemble and even outperformed XGBoost in some city-specific scenarios.

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
