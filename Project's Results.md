 # SARIMAX Model Results: Fuel Price Prediction  

## Overview  
This section highlights the results of the SARIMAX model used to forecast daily fuel prices for the year 2102. It includes key metrics, model diagnostics, and visualizations of the predicted vs. actual values to illustrate the model's accuracy.  

---

## Key Results  

### 1. **Model Performance**  
- **Optimized Parameters**:  
  - ARIMA (p, d, q): (2, 1, 1)  
  - Seasonal (P, D, Q, s): (1, 1, 1, 7)  
- **AIC (Akaike Information Criterion)**: -2683.269  
- **Residual Analysis**: Residuals showed no significant autocorrelation (confirmed by Ljung-Box test).  
![SARIMAX Results](https://github.com/user-attachments/assets/9f273bd5-c494-4a0b-82c7-044bad99553d)


### 2. **Predicted Total Cost**  
The model estimated the **total fuel cost for 2102** to be **$1,757,230**, providing a reliable basis for strategic financial planning.  

---

## Visualization  
 

### 1. **Forecasted Values for 2102**  
The graph demonstrates the predicted daily fuel prices for 2102, incorporating trend and weekly seasonality.  

![Number of Flight in Progress](https://github.com/user-attachments/assets/7fa2d644-500b-4d4f-ab75-235c8a891bb5)

---

## Implications  
The results indicate that the SARIMAX model can accurately forecast fuel prices, enabling businesses to mitigate the risks of price volatility. Future applications may include integrating additional variables or exploring alternative models for even greater precision.  

---

## Next Steps  
- **Share Insights**: Communicate findings with stakeholders for actionable strategies.  
- **Test on New Data**: Apply the model to recent datasets for robustness testing.  
- **Enhance Features**: Include exogenous variables (e.g., economic indicators) for a broader context.  
