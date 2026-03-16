import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Data Science Salary Dashboard",
    layout="wide"
)

# Title
st.title("📊 Data Science Salary Analysis Dashboard (2020–2025)")

# Load Dataset
df = pd.read_csv("feature_engineered_datascience_salaries.csv")

# Sidebar Filters
st.sidebar.header("Filters")

experience = st.sidebar.multiselect(
    "Select Experience Level",
    options=df["experience_level"].unique(),
    default=df["experience_level"].unique()
)

company_size = st.sidebar.multiselect(
    "Select Company Size",
    options=df["company_size"].unique(),
    default=df["company_size"].unique()
)

remote_type = st.sidebar.multiselect(
    "Select Remote Category",
    options=df["remote_category"].unique(),
    default=df["remote_category"].unique()
)

# Apply Filters
filtered_df = df[
    (df["experience_level"].isin(experience)) &
    (df["company_size"].isin(company_size)) &
    (df["remote_category"].isin(remote_type))
]

# KPI Section
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average Salary", f"${int(filtered_df.salary_in_usd.mean()):,}")
col2.metric("Max Salary", f"${int(filtered_df.salary_in_usd.max()):,}")
col3.metric("Total Jobs", len(filtered_df))

# Salary Distribution
st.subheader("Salary Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered_df["salary_in_usd"], kde=True, ax=ax)
st.pyplot(fig)

# Salary by Experience Level
st.subheader("Average Salary by Experience Level")

fig, ax = plt.subplots()
sns.barplot(
    x="experience_level",
    y="salary_in_usd",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# Salary by Company Size
st.subheader("Salary by Company Size")

fig, ax = plt.subplots()
sns.boxplot(
    x="company_size",
    y="salary_in_usd",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# Salary Trend Over Time
st.subheader("Salary Trend (2020–2025)")

trend = filtered_df.groupby("work_year")["salary_in_usd"].mean()

fig, ax = plt.subplots()
trend.plot(marker="o", ax=ax)

st.pyplot(fig)

# Top Job Roles
st.subheader("Top Data Science Roles")

top_roles = (
    filtered_df["job_title"]
    .value_counts()
    .head(10)
)

st.bar_chart(top_roles)

# Salary by Job Category
st.subheader("Salary by Job Category")

fig, ax = plt.subplots()

sns.barplot(
    x="job_category",
    y="salary_in_usd",
    data=filtered_df,
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)