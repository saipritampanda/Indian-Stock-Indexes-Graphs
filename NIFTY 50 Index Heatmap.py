# Import required libraries
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Download NIFTY 50 historical data
nifty = yf.download("^NSEI", start="2021-01-01", end="2025-03-01", auto_adjust=False, progress=False)

# Ensure the index is datetime
nifty.index = pd.to_datetime(nifty.index)

# Get monthly closing price (use 'ME' instead of 'M' to avoid the warning)
nifty_monthly = nifty["Adj Close"].resample("ME").last()

# Compute monthly percentage returns
monthly_returns = nifty_monthly.pct_change() * 100  # Convert to percentage

# Rename column instead of using .to_frame()
monthly_returns_df = monthly_returns.rename(columns={monthly_returns.columns[0]: "Returns"})  

# Extract Year and Month
monthly_returns_df["Year"] = monthly_returns_df.index.year
monthly_returns_df["Month"] = monthly_returns_df.index.month

# Pivot table to create a heatmap matrix
monthly_returns_matrix = monthly_returns_df.pivot_table(
    values="Returns", index="Month", columns="Year"
)

# Rename index (months) for readability
monthly_returns_matrix.index = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Plot heatmap
plt.figure(figsize=(12, 7))
sns.heatmap(
    monthly_returns_matrix, annot=True, cmap="RdYlGn", center=0, 
    fmt=".2f", linewidths=0.5, cbar_kws={"label": "% Monthly Return"}
)

# Titles and Labels
plt