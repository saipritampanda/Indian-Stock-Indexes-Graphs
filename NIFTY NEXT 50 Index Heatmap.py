import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define Index Ticker
index_ticker = "^NSMIDCP"

# Download historical data from 2010 to 2025
index_data = yf.download(index_ticker, start="2010-01-01", end="2025-03-15")

# Ensure "Adj Close" is used or detect the correct column dynamically
if "Adj Close" in index_data.columns:
    index_monthly = index_data["Adj Close"].resample("ME").last()  # Get last price of each month
else:
    index_monthly = index_data.iloc[:, 0].resample("ME").last()  # Use first column if "Adj Close" is missing

# Compute monthly percentage returns
monthly_returns = index_monthly.pct_change() * 100  

# Convert to DataFrame and rename the column
if isinstance(monthly_returns, pd.Series):
    column_name = monthly_returns.name  # Get actual column name
    monthly_returns = monthly_returns.to_frame(name="Returns")
else:
    print("Error: Monthly returns is not a valid Pandas Series")

# Extract Year and Month
monthly_returns["Year"] = monthly_returns.index.year
monthly_returns["Month"] = monthly_returns.index.month

# Pivot table to create a heatmap matrix
monthly_returns_matrix = monthly_returns.pivot_table(values="Returns", index="Month", columns="Year")

# Rename index (months) for readability
monthly_returns_matrix.index = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Plot heatmap
plt.figure(figsize=(12, 7))
sns.heatmap(
    monthly_returns_matrix, annot=True, cmap="RdYlGn", center=0, 
    fmt=".2f", linewidths=0.5, cbar_kws={"label": "% Monthly Return"}
)

# Titles and Labels
plt.title(f"Monthly Returns Heatmap for {index_ticker} (2010-2025)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()
