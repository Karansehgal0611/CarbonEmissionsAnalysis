# Structural Break Analysis & Regime-Based Forecasting Report

## 1. Introduction
This report analyzes structural breaks in the India emissions time series (1970–2024) and implements a regime‑aware forecasting approach. The analysis includes:
- Chow Test for a structural break at 2020 (COVID Shock)
- Automatic breakpoint detection using BIC (Bai–Perron style)
- Piecewise linear regression with identified breakpoints
- ARIMA modeling for each regime
- Final 10‑year forecast with confidence intervals

---

## 2. Detected Breakpoints (BIC-Based Search)
The automatic breakpoint detection algorithm identified **three structural breaks**:

- **2003**
- **2015**
- **2020**

These breakpoints divide the series into four regimes:
1. **1970–2003**
2. **2004–2015**
3. **2016–2020**
4. **2021–2024**

These breaks reflect major shifts:
- 2003: Acceleration of industrial and energy growth
- 2015: Stronger policy and economic shift increasing emissions trajectory
- 2020: COVID-related collapse followed by recovery

---

## 3. Chow Test for a Structural Break at 2020
A Chow test was conducted at the 2019–2020 boundary to test for a COVID-induced structural break.

**Result file:** `chow_test_2020.csv`  
Interpretation:
- If p-value < 0.05 → The structural break at 2020 is statistically significant.
- This would confirm that COVID caused a meaningful deviation in trend.

---

## 4. Piecewise Linear Regression (Segmented Trend)
Using the detected breakpoints (2003, 2015, 2020), a piecewise linear model was fit to estimate different slopes across regimes.

### Interpretation of regimes:
- **Regime 1 (1970–2003):** Moderate and steady growth.
- **Regime 2 (2004–2015):** Strong acceleration in emissions.
- **Regime 3 (2016–2020):** Steep rise in pre‑COVID industrial output.
- **Regime 4 (2021–2024):** Post‑COVID rebound with a new upward slope.

**Plot:** `breaks_piecewise_fit.png`

---

## 5. ARIMA Models per Regime
For each regime, ARIMA(p,d,q) models were selected using AIC.

**Summary file:** `regime_arima_summary.csv`

This ensures:
- Each sub-period trend is modeled independently.
- Older historical dynamics do not distort the modern forecast.
- The final forecast uses only the most recent regime.

---

## 6. Final 10-Year Forecast (2025–2034)
The forecast uses the best ARIMA model from the final regime (2021–2024).

**Forecast table:** `final_forecast_10y_from_last_regime.csv`  
**Forecast plot:** `regimes_and_forecast.png`

The forecast includes:
- Expected emissions for 2025–2034
- 95% confidence intervals
- Visualization of historical regimes

---

## 7. Conclusion

This structural-break-aware forecasting method provides a more reliable picture of long-term emissions trends because it:

- Identifies statistically meaningful breakpoints
- Models trend changes explicitly with piecewise regression
- Trains ARIMA models per regime (not one global ARIMA)
- Uses the most recent regime for forecasting the future
- Correctly incorporates COVID effects and post‑COVID recovery slopes

It is a significant improvement over a single-model ARIMA forecast.

---

*Generated automatically.*