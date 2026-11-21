import pandas as pd

# 1. Create synthetic airline campaign data
data = {
    "campaign": [
        "Google Search",
        "Instagram Ads",
        "Email Marketing"
    ],
    "impressions": [100000, 150000, 40000],
    "clicks": [5000, 4500, 6000],
    "bookings": [250, 135, 420],
    "spend": [2500, 3600, 1200],
    "revenue": [37500, 20250, 63000]
}

df = pd.DataFrame(data)

# 2. Calculate marketing KPIs
df["CTR (%)"] = (
    df["clicks"] / df["impressions"] * 100
)

df["Conversion Rate (%)"] = (
    df["bookings"] / df["clicks"] * 100
)

df["CPA (€)"] = (
    df["spend"] / df["bookings"]
)

df["ROAS"] = (
    df["revenue"] / df["spend"]
)

# 3. Display results
print("\nAIRLINE CAMPAIGN PERFORMANCE")
print(df.round(2).to_string(index=False))

# 4. Identify the best campaigns
print("\nBEST PERFORMING CAMPAIGNS")

print(
    "Highest CTR:",
    df.loc[df["CTR (%)"].idxmax(), "campaign"]
)

print(
    "Highest Conversion Rate:",
    df.loc[df["Conversion Rate (%)"].idxmax(), "campaign"]
)

print(
    "Lowest CPA:",
    df.loc[df["CPA (€)"].idxmin(), "campaign"]
)

print(
    "Highest ROAS:",
    df.loc[df["ROAS"].idxmax(), "campaign"]
)
