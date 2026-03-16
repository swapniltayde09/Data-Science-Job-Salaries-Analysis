📊 Data Science Salary Analysis & Prediction (2020–2025)

End-to-end Data Analytics project analyzing global Data Science salary trends using Python.
The project explores key factors influencing compensation and builds a salary prediction model using machine learning.

This project demonstrates a complete data analytics workflow including data cleaning, feature engineering, exploratory analysis, visualization, and predictive modeling.

🚀 Project Overview

The demand for data science professionals has grown rapidly in recent years. This project analyzes salary data to answer key questions:

What factors influence data science salaries?

Which roles command the highest compensation?

How do salaries vary by experience, company size, and location?

Can salaries be predicted using job-related features?

The analysis uses Python-based data science tools to uncover patterns and generate business insights.

📂 Project Structure
DataScience-Salary-Analysis
│
├── data
│   ├── DataScience_salaries_cleaned.csv
│   ├── cleaned_datascience_salaries.csv
│   ├── feature_engineered_datascience_salaries.csv
│
├── outputs
│   ├── average_salary_by_location.csv
│   ├── average_salary_top_roles.csv
│   ├── salary_by_company.csv
│   ├── salary_by_experience.csv
│   ├── salary_by_role.csv
│   ├── salary_trend.csv
│
├── visualizations
│   ├── salary_distribution.png
│   ├── salary_trend.png
│   ├── job_role_analysis.png
│
├── notebooks / scripts
│   ├── datascience_salaries_eda_final.py
│
└── reports
    ├── presentation.pptx
    ├── analytics_report.docx
🧰 Tools & Technologies

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn

These tools were used for data preprocessing, visualization, statistical analysis, and machine learning modeling.

🔄 Data Analytics Pipeline

The project follows a structured analytics workflow:

Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Correlation Analysis
     ↓
Machine Learning Model
     ↓
Business Insights
     ↓
Dashboard & Reports
🧹 Data Cleaning & Preparation

Key preprocessing steps:

Checked dataset structure using .info(), .describe()

Handled missing values

Removed duplicate records

Standardized column names

Converted categorical data types

Standardized salaries using salary_in_usd

Reset dataset index and exported cleaned data

⚙️ Feature Engineering

New analytical features were created to improve insights and modeling:

experience_level_num

company_size_num

remote_category

salary_band

job_category

years_since_2020

log_salary

These engineered features allow deeper analysis of salary drivers.

📊 Exploratory Data Analysis (EDA)

EDA was performed to understand salary patterns using visualizations.

Key analyses include:

Salary Distribution

Understanding salary ranges and outliers.

Experience Level Distribution

Comparing salaries across Entry, Mid, Senior, and Executive roles.

Employment Type Analysis

Full-time vs contract vs freelance roles.

Company Size Analysis

Salary variations across small, medium, and large companies.

Remote Work Trends

Impact of remote work on compensation.

Top Data Science Job Roles

Identifying the most common roles in the dataset.

🔎 Correlation Analysis

Correlation heatmaps and pairplots were used to examine relationships between variables such as:

Experience level

Company size

Remote ratio

Salary

Key finding:

Experience level shows the strongest correlation with salary.

🤖 Salary Prediction Model

A Linear Regression model was built using Scikit-Learn to predict salaries.

Features used

Experience level

Company size

Remote work ratio

Years since 2020

Model workflow
Train/Test Split
↓
Linear Regression Model
↓
Prediction
↓
Model Evaluation
Evaluation Metrics

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

📈 Key Insights
1️⃣ Experience Level Drives Salary

Senior and executive professionals earn significantly more than entry-level roles.

2️⃣ Specialized Roles Pay More

High-paying roles include:

Machine Learning Engineer

AI Engineer

Applied Scientist

Data Science Manager

3️⃣ Large Companies Offer Higher Compensation

Larger organizations typically offer higher salaries due to scale and infrastructure complexity.

4️⃣ Remote Work Does Not Reduce Salary

Remote roles often pay competitively with on-site positions.

5️⃣ Salaries Are Increasing Over Time

Data science salaries have steadily increased between 2020 and 2025.

📊 Dashboard & Reports

The project includes:

Analytics PowerPoint presentation

Portfolio-grade consulting report

CSV summary reports for dashboards

Example reports:

Salary by experience level

Salary by company size

Salary by role

Salary trend over time

📌 Business Impact

The analysis helps organizations:

Benchmark salary offers

Understand data talent market trends

Design competitive compensation strategies

Plan hiring strategies for data teams

🔮 Future Improvements

Potential extensions of the project:

Use advanced models (Random Forest, XGBoost)

Build interactive dashboards (Power BI / Tableau)

Add more datasets from job portals

Include cost-of-living adjustments

👤 Skills demonstrated:

Data Cleaning

Exploratory Data Analysis

Feature Engineering

Data Visualization

Machine Learning

Business Insights
