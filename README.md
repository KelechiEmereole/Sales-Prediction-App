## Sales Prediction App  

 **[Live Demo on Streamlit](https://sales-prediction-app-gwkuaeh2rjasp2aopvivah.streamlit.app/)**

### Project Overview

This project builds and deploys a Machine Learning web application that predicts supermarket sales. The app is designed using Streamlit and powered by a Gradient Boosting Regressor model, carefully chosen after evaluating multiple regression techniques.

### STAR Breakdown

### Situation
Supermarkets handle large volumes of transactions daily, making it crucial to predict sales accurately. Businesses need insights into sales drivers such as customer demographics, branch location, and product categories to optimize inventory and improve decision-making.

### Task

My task was to:

* Analyze supermarket sales data.

* Build, compare, and evaluate different regression models.

* Deploy the best-performing model into a user-friendly web app using Streamlit.

### Action

#### Exploratory Data Analysis (EDA):

Analyzed sales across gender, branch, city, product line, and customer type.

Found interesting patterns such as higher total sales for Female customers and Naypyitaw being the top-performing city.

Transformed skewed features with log transformation for better model performance.

### Modeling (5 regression models):

Linear Regression → R² = 0.93

Decision Tree Regressor (Tuned) → R² = 0.99

Random Forest Regressor (Tuned) → R² = 0.96

Support Vector Regressor (Tuned) → R² = 0.93

Gradient Boosting Regressor (Tuned) → R² = 1.00 ✅

Model Selection:

Gradient Boosting Regressor delivered the lowest MAE (5.37) and lowest RMSE (12.78), making it the most accurate and robust model.

Deployment:

Designed a Streamlit app where users can input customer details (gender, branch, city, customer type, product line, unit price, quantity, and tax) and instantly get a predicted sales value.

### Result

Built a production-ready ML app that predicts sales with ~100% accuracy (R² = 1.0) on test data.

Created clear insights for supermarket managers:

Female customers generate slightly higher sales.

Naypyitaw branch leads in total revenue.

Fashion accessories & Sports and travel are the top-selling product lines.

Enhanced my expertise in model evaluation, hyperparameter tuning, and real-world deployment with Streamlit.

#### Model Performance Comparison

Model                   |    	       MAE	         |  RMSE	 |   R²

Linear Regression	     |              64.40	       |  81.97	 |  0.93

Decision Tree Regressor (Tuned)	   |  6.90	       |   22.58	 | 0.99

Random Forest Regressor (Tuned)	   |  30.73	     |    57.50	   | 0.96

Support Vector Regressor	      |     63.81	    |     81.87	  |   0.93

Gradient Boosting Regressor (Tuned)	 |  5.37	      |    12.78	  |  1.00 

###  Key Business Insights & Recommendations

#### Product Line

Insight: Fashion Accessories led with the highest total sales of ₦62,055.88, followed by Sports and Travel (₦59,979.22) and Home and Lifestyle (₦58,948.28).
Recommendation: Increase marketing and inventory for Fashion Accessories. Explore cross-selling opportunities with Sports & Travel to maximize revenue.

#### Gender

Insight: Female customers contributed ₦182,578.11, higher than Male customers at ₦168,920.66.
Recommendation: Tailor promotions toward female customers, while designing strategies (e.g., loyalty bonuses) to boost male customer spending.

#### City & Branch

Insight: Naypyitaw (Branch C) generated the highest sales (₦121,351.11), followed by Yangon (₦116,366.95) and Mandalay (₦113,780.72).
Recommendation: Invest in customer retention programs in Naypyitaw. Offer targeted promotions in Yangon and Mandalay to close the gap.

#### Customer Type

Insight: Members generated higher sales (₦179,208.41) compared to Normal (non-member) customers (₦172,290.36).
Recommendation: Strengthen membership programs with exclusive deals to convert more Normal customers into Members.

#### Quantity Purchased

Insight: Bulk purchases of 10 items contributed the highest total sales (₦69,928.95).
Recommendation: Introduce bundle deals or bulk purchase discounts to encourage higher-volume transactions.

#### Tech Stack

Python (Pandas, NumPy, Scikit-learn)

Machine Learning Models: Linear Regression, Decision Tree, Random Forest, Support Vector Regression, Gradient Boosting

Streamlit (for deployment)

Matplotlib / Seaborn (for visualization)

Joblib (for model persistence)


**Thank you for taking the time to read this report!**

**Please reach out for any updates.**

### Author
[Kelechi Emereole](https://github.com/KelechiEmereole)
