
import streamlit as st
import pandas as pd
import plotly.express as px

# Define the data with corrected date formats

data = [
    {"Date": "2021-01-01", "Event": "Biden takes office", "Impact": "Status quo; industrials absorb elevated input costs.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2024-09-01", "Event": "Biden raises average tariff to 20.8%", "Impact": "Cost pressure increases; firms reassess sourcing.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2024-09-01", "Event": "Biden raises average tariff to 20.8%", "Impact": "Cost pressure increases; firms reassess sourcing.", "Country": "Mexico", "Import Share (%)": 13, "Dollar Impact(Billions)": 260},
    {"Date": "2024-09-01", "Event": "Biden raises average tariff to 20.8%", "Impact": "Cost pressure increases; firms reassess sourcing.", "Country": "Canada", "Import Share (%)": 12, "Dollar Impact(Billions)": 240},
    {"Date": "2024-05-14", "Event": "Biden expands Section 301 tariffs", "Impact": "Construction & green tech sectors hit hardest.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2025-02-04", "Event": "Trump imposes 10% tariff on all Chinese imports", "Impact": "Machinery & electronics costs spike.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2025-03-04", "Event": "Adds another 10%, total 20%", "Impact": "Margins tighten; reshoring discussions intensify.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2025-04-02", "Event": "Launches 34% “Reciprocal Tariff”", "Impact": "Total 54% tariff; severe raw material inflation.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2025-04-17", "Event": "Tariff war escalates to 245%", "Impact": "Supply chains freeze; construction delays spike.", "Country": "China", "Import Share (%)": 19, "Dollar Impact(Billions)": 380},
    {"Date": "2025-05-12", "Event": "Geneva Deal: 90-day pause", "Impact": "Temporary relief; firms explore nearshoring.", "Country": "Mexico", "Import Share (%)": 13, "Dollar Impact(Billions)": 260},
    {"Date": "2025-05-12", "Event": "Geneva Deal: 90-day pause", "Impact": "Temporary relief; firms explore nearshoring.", "Country": "Canada", "Import Share (%)": 12, "Dollar Impact(Billions)": 240},
    {"Date": "2025-07-09", "Event": "Tariff suspension on non-China partners expires", "Impact": "North American steel & aluminum costs surge.", "Country": "Canada", "Import Share (%)": 12, "Dollar Impact(Billions)": 240},
    {"Date": "2025-07-12", "Event": "New tariffs: 30% (EU/Mexico), 35% (Canada), 50% (Brazil, copper)", "Impact": "Copper-intensive sectors hit hard.", "Country": "Brazil", "Import Share (%)": 5, "Dollar Impact(Billions)": 100},
    {"Date": "2025-07-18", "Event": "Trump warns of Aug 1 tariff barrage", "Impact": "Automation & electronics sectors brace for impact.", "Country": "Taiwan", "Import Share (%)": 4, "Dollar Impact(Billions)": 80},
    {"Date": "2025-07-18", "Event": "Trump warns of Aug 1 tariff barrage", "Impact": "Automation & electronics sectors brace for impact.", "Country": "South Korea", "Import Share (%)": 4, "Dollar Impact(Billions)": 80}
]



# Convert to DataFrame
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Streamlit UI
st.title("U.S.–China Tariff Timeline & Industrials Impact")

# Filters
date_range = st.slider("Select Date Range", min_value=df["Date"].min().date(), max_value=df["Date"].max().date(), value=(df["Date"].min().date(), df["Date"].max().date()))
selected_country = st.multiselect("Select Country", options=df["Country"].unique(), default=list(df["Country"].unique()))
selected_impact = st.multiselect("Select Impact Keywords", options=df["Impact"].unique(), default=list(df["Impact"].unique()))

# Filter data
filtered_df = df[
    (df["Date"].dt.date >= date_range[0]) &
    (df["Date"].dt.date <= date_range[1]) &
    (df["Country"].isin(selected_country)) &
    (df["Impact"].isin(selected_impact))
]

# Scatter plot
fig = px.scatter(
    filtered_df,
    x="Date",
    y="Import Share (%)",
    color="Country",
    hover_data=["Event", "Impact"],
    title="Tariff Events and Industrial Import Exposure"
)
st.plotly_chart(fig)
# Time series plot of dollar impact
impact_over_time = filtered_df.groupby("Date")["Dollar Impact(Billions)"].sum().reset_index()
impact_fig = px.line(
    impact_over_time,
    x="Date",
    y="Dollar Impact(Billions)",
    title="Estimated Dollar Impact to Industrials Over Time"
)
st.plotly_chart(impact_fig)

# Data table
st.subheader("Filtered Events")
st.dataframe(filtered_df.sort_values("Date"))



