import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame with all the tariff actions
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

# Create the DataFrame
df = pd.DataFrame(data, columns=["Date", "Action", "Target", "Type", "Percentage", "Affected Industries"])
df["Date"] = pd.to_datetime(df["Date"])

# Summary statistics
type_counts = df["Type"].value_counts()
average_tariff = df["Percentage"].dropna().mean()

print("Summary Statistics:")
print("Number of Tariff Actions by Type:")
print(type_counts)
print(f"\nAverage Tariff Percentage (excluding None): {average_tariff:.2f}%")

# Timeline of actions
df_sorted = df.sort_values("Date")
print("\nTimeline of Tariff Actions:")
print(df_sorted[["Date", "Action", "Type"]])

# Visualization: Number of actions by type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Type", order=type_counts.index, palette="Set2")
plt.title("Number of Tariff Actions by Type")
plt.xlabel("Action Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("tariff_actions_by_type.png")
plt.close()

# Visualization: Affected industries
industry_series = df["Affected Industries"].dropna().str.split(", ").explode()
industry_counts = industry_series.value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=industry_counts.values, y=industry_counts.index, palette="Set3")
plt.title("Affected Industries by Tariff Actions")
plt.xlabel("Number of Mentions")
plt.ylabel("Industry")
plt.tight_layout()
plt.savefig("affected_industries.png")
plt.close()

# Visualization: Targeted countries/regions
target_series = df["Target"].dropna().str.split(", ").explode()
target_counts = target_series.value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=target_counts.values, y=target_counts.index, palette="Set1")
plt.title("Targeted Countries/Regions by Tariff Actions")
plt.xlabel("Number of Mentions")
plt.ylabel("Country/Region")
plt.tight_layout()
plt.savefig("targeted_countries.png")
plt.close()
