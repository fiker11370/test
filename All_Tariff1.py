import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page config
st.set_page_config(page_title="Tariff Actions Dashboard", layout="wide")

# Data
data = [
    ["Jan 20, 2025", "Announced 25% tariffs on Canada and Mexico", "Canada, Mexico", "Threat", 25, "Consumer Products, Industrials"],
    ["Jan 20, 2025", "Proposed 10% tariff on all Chinese imports", "China", "Threat", 10, "Tech, Media & Telecommunications, Consumer Products, Industrials"],
    ["Jan 26, 2025", "Threatened 25% tariffs on Colombia", "Colombia", "Threat", 25, "Consumer Products, Industrials"],
    ["Feb 1, 2025", "Signed EO for 10% tariffs on Chinese goods", "China", "Imposed", 10, "Tech, Media & Telecommunications, Consumer Products, Industrials"],
    ["Feb 1, 2025", "Signed EO for 25% tariffs on Canada and Mexico", "Canada, Mexico", "Threat", 25, "Consumer Products, Industrials"],
    ["Feb 3, 2025", "Paused 25% tariffs on Canada and Mexico for 30 days", "Canada, Mexico", "Paused", 25, "Consumer Products, Industrials"],
    ["Feb 4, 2025", "10% tariffs on Chinese goods take effect", "China", "Imposed", 10, "Tech, Media & Telecommunications, Consumer Products"],
    ["Feb 10, 2025", "Announced 25% tariffs on steel and aluminum", "Global", "Threat", 25, "Industrials"],
    ["Feb 13, 2025", "Proposed reciprocal tariffs on countries taxing U.S. goods", "Various", "Threat", None, "Consumer Products, Tech, Media & Telecommunications"],
    ["Feb 25, 2025", "Ordered tariff probe into copper imports", "Global", "Threat", None, "Industrials"],
    ["Mar 4, 2025", "Raised Chinese tariffs to 20%", "China", "Imposed", 20, "Tech, Media & Telecommunications, Consumer Products"],
    ["Mar 4, 2025", "25% tariffs on Canada and Mexico take effect", "Canada, Mexico", "Imposed", 25, "Consumer Products, Industrials"],
    ["Mar 5, 2025", "Granted 30-day exemption to Canada and Mexico", "Canada, Mexico", "Paused", 25, "Consumer Products, Industrials"],
    ["Mar 12, 2025", "Steel and aluminum tariffs take effect", "Global", "Imposed", 25, "Industrials"],
    ["Mar 13, 2025", "Threatened 200% tariffs on European wines and spirits", "EU", "Threat", 200, "Consumer Products"],
    ["Mar 24, 2025", "Announced 25% tariffs on countries buying Venezuelan oil/gas", "Various", "Threat", 25, "Industrials, State & Local Government"],
    ["Apr 2, 2025", "Announced 10% universal tariff on all imports", "Global", "Threat", 10, "Consumer Products, Tech, Media & Telecommunications, Industrials, Real Estate"],
    ["Apr 3, 2025", "25% tariff on foreign-made cars takes effect", "Global", "Imposed", 25, "Consumer Products, Industrials"],
    ["Apr 5, 2025", "10% universal tariff takes effect", "Global", "Imposed", 10, "Consumer Products, Tech, Media & Telecommunications, Industrials, Real Estate"],
    ["Apr 9, 2025", "Raised Chinese tariffs from 104% to 145%", "China", "Imposed", 145, "Tech, Media & Telecommunications, Consumer Products"],
    ["Apr 9, 2025", "90-day pause on other new tariffs (except China)", "Global (except China)", "Paused", None, "Consumer Products, Tech, Media & Telecommunications, Industrials, Real Estate"],
    ["Aug 1, 2025", "Scheduled new tariffs: 25% on Japan & South Korea, up to 50% on others", "Japan, South Korea, others", "Threat", 50, "Tech, Media & Telecommunications, Consumer Products, Industrials"]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Action", "Target", "Type", "Percentage", "Affected Industries"])
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.slider("Select Date Range", min_value=df["Date"].min().date(), max_value=df["Date"].max().date(), value=(df["Date"].min().date(), df["Date"].max().date()))
selected_type = st.sidebar.multiselect("Select Action Type", df["Type"].unique(), default=list(df["Type"].unique()))

# Filtered DataFrame
filtered_df = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1])]
filtered_df = filtered_df[filtered_df["Type"].isin(selected_type)]

# Summary
st.title("📊 Tariff Actions Dashboard")
st.markdown(f"**Total Actions:** {len(filtered_df)}")
st.markdown(f"**Average Tariff (excluding None):** {filtered_df['Percentage'].dropna().mean():.2f}%")

# Timeline
st.subheader("🕒 Timeline of Tariff Actions")
st.dataframe(filtered_df.sort_values("Date")[["Date", "Action", "Type"]])

# Plot: Actions by Type
st.subheader("📌 Tariff Actions by Type Over Time")
type_time = filtered_df.groupby([filtered_df["Date"].dt.to_period("M"), "Type"]).size().unstack(fill_value=0)
st.line_chart(type_time)

# Plot: Affected Industries
st.subheader("🏭 Affected Industries Over Time")
industry_df = filtered_df.dropna(subset=["Affected Industries"]).copy()
industry_df["Date"] = industry_df["Date"].dt.to_period("M")
industry_df = industry_df.assign(Industry=industry_df["Affected Industries"].str.split(", ")).explode("Industry")
industry_time = industry_df.groupby(["Date", "Industry"]).size().unstack(fill_value=0)
st.line_chart(industry_time)

# Plot: Targeted Countries
st.subheader("🌍 Targeted Countries/Regions Over Time")
target_df = filtered_df.dropna(subset=["Target"]).copy()
target_df["Date"] = target_df["Date"].dt.to_period("M")
target_df = target_df.assign(Country=target_df["Target"].str.split(", ")).explode("Country")
target_time = target_df.groupby(["Date", "Country"]).size().unstack(fill_value=0)
st.line_chart(target_time)

# Embed the updated map
st.subheader("🗺️ Imposed Tariff Map")
map_url = "https://raw.githubusercontent.com/fiker11370/test/main/tariff_map.html"
components.iframe(map_url, height=600, scrolling=True)
