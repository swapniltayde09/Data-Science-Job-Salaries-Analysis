# Run the Streamlit Interactive Dashboard Locally

This guide explains how to run the **Data Science Salary Analysis
Streamlit Dashboard** on your local machine.

------------------------------------------------------------------------

# 1. Prerequisites

Make sure the following are installed:

-   Python 3.8 or higher
-   pip (Python package manager)
-   Git (optional but recommended)

Check your Python version:

``` bash
python --version
```

------------------------------------------------------------------------

# 2. Clone the Repository

Clone the GitHub repository to your local machine.

``` bash
git clone https://github.com/your-username/data-science-salary-analysis.git
```

Navigate into the project folder:

``` bash
cd data-science-salary-analysis
```

------------------------------------------------------------------------

# 3. Create a Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies.

``` bash
python -m venv venv
```

Activate the environment.

### Windows

``` bash
venv\Scripts\activate
```

### macOS / Linux

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

# 4. Install Required Libraries

Install all required Python packages.

``` bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```

------------------------------------------------------------------------

# 5. Verify Dataset Location

Ensure the dataset file exists in the correct directory.

Expected structure:

    project-folder
    │
    ├── data
    │   └── feature_engineered_datascience_salaries.csv
    │
    ├── dashboard
    │   └── streamlit_dashboard.py

If necessary, update the dataset path in the script.

Example:

``` python
df = pd.read_csv("data/feature_engineered_datascience_salaries.csv")
```

------------------------------------------------------------------------

# 6. Run the Streamlit Application

Navigate to the dashboard folder.

``` bash
cd dashboard
```

Run the Streamlit application.

``` bash
streamlit run streamlit_dashboard.py
```

------------------------------------------------------------------------

# 7. Open the Dashboard in Your Browser

After running the command, Streamlit will automatically launch the
dashboard.

Default URL:

    http://localhost:8501

------------------------------------------------------------------------

# 8. Dashboard Features

The dashboard includes:

-   Interactive filters
-   Salary distribution analysis
-   Salary trends over time
-   Salary comparison by experience level
-   Salary comparison by company size
-   Top data science job roles
-   Salary analysis by job category

------------------------------------------------------------------------

# 9. Troubleshooting

### Streamlit not recognized

Install Streamlit again:

``` bash
pip install streamlit
```

### Port already in use

Run Streamlit on another port:

``` bash
streamlit run streamlit_dashboard.py --server.port 8502
```

------------------------------------------------------------------------

# 10. Stop the Application

To stop the dashboard, press:

    CTRL + C

------------------------------------------------------------------------

# 11. Optional: Deploy the Dashboard

You can deploy the Streamlit dashboard using:

-   Streamlit Community Cloud
-   Render
-   AWS
-   Heroku

Deployment allows others to interact with your dashboard online.

------------------------------------------------------------------------

# Project Outcome

This dashboard allows users to explore **global data science salary
trends interactively**, providing insights into:

-   Salary drivers
-   Job role compensation patterns
-   Company size influence
-   Remote work trends
-   Market growth over time

