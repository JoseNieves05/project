import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

csv_url = "https://ourworldindata.org/grapher/share-artificial-intelligence-job-postings.csv?v=1&csvType=full&useColumnShortNames=true"

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_url)

# Optional: display the first few rows of the DataFrame
st.write("Preview of the data:", df.head())

# Create a Plotly line chart.
# Adjust the x, y, and color parameters according to your CSV's actual column names.
fig = px.line(
    df,
    x="Year",  # Column for the time axis (adjust if necessary)
    y="Share of artificial intelligence jobs among all job postings",  # Metric column (adjust if necessary)
    color="Entity",  # Column for the categories (e.g., countries)
    title="Share of artificial intelligence jobs among all job postings"
)

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)
