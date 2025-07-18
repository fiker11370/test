
import pandas as pd
import plotly.express as px
import streamlit as st

# Sample data for tariff events
tariff_data = pd.DataFrame({
    "Date": [
        "2021-01-20", "2024-09-01", "2024-05-14", "2025-02-04", "2025-03-04",
        "2025-04-02", "2025-04-17", "2025-05-12", "2025-07-07", "2025-07-12"
    ],
    "Event": [
        "Biden takes office", "Tariff raised to 20.8%", "Section 301 expansion",
        "10% tariff on China", "Additional 10% tariff", "34% Reciprocal Tariff",
        "Tariffs escalate to 245%", "Geneva Deal - 30% tariff", 
        "Tariff extension to Aug 1", "New tariffs on EU, Canada, Brazil"
    ],
    "Country": [
        "USA", "China", "China", "China", "China", "China", "China", "China", "USA", "Multiple"
    ],
    "Impact Type": [
        "Policy", "Tariff", "Tariff", "Tariff", "Tariff", "Tariff", "Tariff", "Relief", "Tariff", "Tariff"
    ]
})

# Sample monetary impact data
monetary_impact_data = pd.DataFrame({
    "Date": pd.to_datetime([
        "2024-09-01", "2025-02-04", "2025-03-04", "2025-04-02", "2025-04-17", "2025-05-12", "2025-07-07", "2025-07-12"
    ]),
    "China": [5.2, 6.8, 8.1, 10.5, 12.0, 9.5, 10.2, 11.0],
    "Canada": [1.0, 1.2, 1.3, 1.5, 1.7, 1.4, 2.0, 2.5],
    "Brazil": [0.5, 0.6, 0.7, 0.9, 1.0, 0.8, 1.1, 1.3],
    "EU": [2.0, 2.2, 2.5, 2.8, 3.0, 2.6, 3.2, 3.5]
})

# Streamlit app
st.title("U.S.–China Tariff Timeline and Industrial Impact")

# Timeline chart with country markers
fig_timeline = px.scatter(
    tariff_data,
    x="Date",
    y=["Impact Type"] * len(tariff_data),
    color="Country",
    hover_name="Event",
    title="Tariff Events Timeline by Country"
)
st.plotly_chart(fig_timeline)

# Line chart for monetary impact
impact_df = monetary_impact_data.set_index("Date")
fig_impact = px.line(
    impact_df,
    title="Estimated Monetary Impact on Industrial Businesses (in Billion USD)",
    labels={"value": "Impact (B USD)", "variable": "Country"}
)
st.plotly_chart(fig_impact)
