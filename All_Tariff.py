import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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
selected_type = st.sidebar.multiselect("Select Action Type", df["Type"].unique(), default=df["Type"].unique())

# Filtered DataFrame
filtered_df = df[df["Type"].isin(selected_type)]

# Summary
st.title("📊 Tariff Actions Dashboard")
st.markdown(f"**Total Actions:** {len(filtered_df)}")
st.markdown(f"**Average Tariff (excluding None):** {filtered_df['Percentage'].dropna().mean():.2f}%")

# Timeline
st.subheader("🕒 Timeline of Tariff Actions")
st.dataframe(filtered_df.sort_values("Date")[["Date", "Action", "Type"]])

# Plot: Actions by Type
st.subheader("📌 Number of Tariff Actions by Type")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x="Type", order=filtered_df["Type"].value_counts().index, ax=ax1, palette="Set2")
st.pyplot(fig1)

# Plot: Affected Industries
st.subheader("🏭 Affected Industries")
industry_series = filtered_df["Affected Industries"].dropna().str.split(", ").explode()
industry_counts = industry_series.value_counts()
fig2, ax2 = plt.subplots()
sns.barplot(x=industry_counts.values, y=industry_counts.index, ax=ax2, palette="Set3")
st.pyplot(fig2)

# Plot: Targeted Countries
st.subheader("🌍 Targeted Countries/Regions")
target_series = filtered_df["Target"].dropna().str.split(", ").explode()
target_counts = target_series.value_counts()
fig3, ax3 = plt.subplots()
sns.barplot(x=target_counts.values, y=target_counts.index, ax=ax3, palette="Set1")
st.pyplot(fig3)
