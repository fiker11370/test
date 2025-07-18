
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Sample data for the timeline with country flags and monetary impact
data = [
    {"Date": "2021-01-20", "Event": "Biden takes office", "Country": "USA", "Impact": "Status quo", "ImportShare": 0.0, "MonetaryImpact": 0},
    {"Date": "2024-09-01", "Event": "Biden raises tariffs", "Country": "China", "Impact": "Cost pressure", "ImportShare": 19, "MonetaryImpact": 5},
    {"Date": "2024-11-05", "Event": "Trump wins election", "Country": "USA", "Impact": "Uncertainty", "ImportShare": 0.0, "MonetaryImpact": 0},
    {"Date": "2025-02-04", "Event": "10% tariff on China", "Country": "China", "Impact": "Input cost spike", "ImportShare": 19, "MonetaryImpact": 15},
    {"Date": "2025-03-04", "Event": "Additional 10% tariff", "Country": "China", "Impact": "Margins tighten", "ImportShare": 19, "MonetaryImpact": 25},
    {"Date": "2025-04-02", "Event": "34% Reciprocal Tariff", "Country": "China", "Impact": "Raw material inflation", "ImportShare": 19, "MonetaryImpact": 40},
    {"Date": "2025-05-12", "Event": "Geneva Deal", "Country": "China", "Impact": "Temporary relief", "ImportShare": 19, "MonetaryImpact": 30},
    {"Date": "2025-07-12", "Event": "New tariffs on Brazil", "Country": "Brazil", "Impact": "Copper cost spike", "ImportShare": 5, "MonetaryImpact": 35},
]

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Mapping countries to flag emojis
flag_map = {
    "USA": "🇺🇸",
    "China": "🇨🇳",
    "Brazil": "🇧🇷"
}
df["Flag"] = df["Country"].map(flag_map)

# Streamlit app
st.title("U.S.–China Tariff Timeline and Industrials Impact")

# Scatter plot with flags as text markers
fig = go.Figure()
for _, row in df.iterrows():
    fig.add_trace(go.Scatter(
        x=[row["Date"]],
        y=[row["ImportShare"]],
        mode="text",
        text=[row["Flag"]],
        textposition="top center",
        hovertext=f"{row['Date'].date()}<br>{row['Event']}<br>{row['Impact']}",
        hoverinfo="text"
    ))

fig.update_layout(
    title="Tariff Events with Country Flags",
    xaxis_title="Date",
    yaxis_title="Import Share (%)",
    yaxis=dict(range=[0, 25]),
    showlegend=False
)

st.plotly_chart(fig)

# Line chart for monetary impact
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(
    x=df["Date"],
    y=df["MonetaryImpact"],
    mode="lines+markers",
    name="Monetary Impact",
    line=dict(color="firebrick", width=3)
))

line_fig.update_layout(
    title="Estimated Monetary Impact on Industrials Sector",
    xaxis_title="Date",
    yaxis_title="Impact (Billion USD)",
    yaxis=dict(range=[0, max(df["MonetaryImpact"]) + 10])
)

st.plotly_chart(line_fig)
