# Optimizing Fuel Price Predictions Using SARIMAX  

## Project Overview  
This project focuses on developing an advanced time series forecasting model to predict daily fuel prices for the year 2102. Using historical data from 2101, the goal was to model price trends and seasonality to provide accurate future estimates. The results of this project offer actionable insights for industries reliant on fuel price fluctuations.  

---

## Problem Statement  
Fuel price volatility impacts operational planning and budgeting for businesses. Predicting future fuel prices accurately is essential for strategic decision-making, cost optimization, and reducing financial risks. This project addresses the challenge of forecasting daily fuel prices, incorporating both trend and weekly seasonality.  

---

## Methodology  

### 1. **Data Collection and Exploration**  
The dataset contained daily fuel prices for 2101. Initial steps included data exploration to understand patterns, trends, and seasonality.  
Key considerations:  
- Checked for missing values and handled them using forward-fill to ensure continuity in time series.  
- Verified chronological order to maintain temporal integrity.  

### 2. **Data Preparation**  
Data preprocessing steps were essential to prepare the dataset for modeling:  
- Assessed stationarity using the Augmented Dickey-Fuller test and differenced the data to eliminate trends.  
- Decomposed the series to confirm the presence of weekly seasonality.  
- Normalized values to stabilize variance and improve model performance.  

### 3. **Model Selection and Configuration**  
The SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors) model was chosen for its ability to capture both trend and seasonal components.  
- Identified initial parameters using grid search and evaluated based on the AIC criterion.  
- Incorporated weekly seasonality with a seasonal lag of 7.  
- Fine-tuned parameters for AR (AutoRegressive), I (Integrated), and MA (Moving Average) terms to balance model complexity and performance.  

### 4. **Model Training and Evaluation**  
- Trained the SARIMAX model on the prepared dataset.  
- Evaluated the model using metrics like AIC, BIC, and Ljung-Box tests to assess goodness-of-fit and residual behavior.  
- Validated predictions by visualizing residuals and comparing predicted values against actual prices.  

---

## Results  
- Achieved a highly optimized model with an AIC of -2683.269.  
- Predicted fuel prices for 2102 with high precision.  
- Estimated total fuel costs for 2102: **$1,757,230**.  
- Residual diagnostics confirmed no significant autocorrelation, validating the robustness of the model.  

---

## Challenges and Solutions  

### 1. **Data Stationarity**  
Ensuring stationarity was a critical challenge. This required differencing the data and iterative adjustments to the seasonal and trend parameters.  

### 2. **Parameter Tuning**  
Hyperparameter optimization for SARIMAX is computationally expensive. A combination of automated grid search and manual adjustments ensured optimal performance.  

### 3. **Model Convergence**  
The SARIMAX model occasionally faced convergence issues. Adjusting solver parameters and carefully initializing coefficients helped address this.  

### 4. **Handling Seasonality**  
Incorporating the weekly seasonality component required significant testing and validation to ensure it was accurately captured in the model.  

---

## Implications  
The success of this project demonstrates the power of time series modeling in predicting future trends. Accurate forecasts can help industries optimize resource allocation, budgeting, and strategic planning. For businesses heavily influenced by fuel prices, this model provides a reliable tool for mitigating financial risks.  

---

## Future Work  
- Explore additional exogenous variables (e.g., economic indicators, geopolitical events) to improve prediction accuracy.  
- Test alternative models like Prophet or LSTM for comparative analysis.  
- Automate hyperparameter tuning for efficiency in larger datasets.  

---

## Conclusion  
This project highlights the intricacies of time series forecasting, from data preparation to advanced modeling with SARIMAX. By overcoming challenges and delivering precise predictions, the work demonstrates the value of data-driven insights for real-world decision-making.  

---  

## Repository Structure  
- **Code**: Main implementation files for data preparation, modeling, and evaluation.     
- **Results**: Outputs, including forecasted values and visualizations.
