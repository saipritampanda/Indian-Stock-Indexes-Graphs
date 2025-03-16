## Historical Monthly Percentage Changes of Indian Stock Indexes Graphs (Heatmaps), using Yahoo Finance API

This project utilizes the `yfinance` library to fetch historical and real-time stock data and analyze it using Python, and show the Heatmaps in terms of % for each month. It includes visualization tools to help interpret stock trends.

## Indexes Analyzed:
1. NIFTY 50 - `^NSEI`
2. NIFTY NEXT 50 - `^NSMIDCP`

## Installation

Before running the script, ensure that you have the necessary libraries installed. You can install them using the following command:

```bash
pip install yfinance pandas numpy seaborn matplotlib --quiet
```

## Running on Google Colab
This project includes optimized scripts that provide better performance when executed in Google Colab.

To run in Colab:

1. Open Google Colab: Google Colab
2. Upload the respective code from this repository.
3. Run the cells to execute the analysis.

## Date Range

- MAX Start Date: `Index Launch Date`
- End Date: `Today's Date / Index Termination Date`

## Dependencies Used

- `yfinance` - Fetches stock market data.  
- `pandas` - Handles data processing.  
- `numpy` - Performs numerical computations.  
- `seaborn` & `matplotlib` - Used for data visualization.

## Heatmaps

- **NIFTY 50 :**

| NIFTY 50 HeatMap (2010 - 2025) |
|--------------------------------|
| <img src="HeatMaps Screenshots/NIFTY 50/NIFTY 50 HeatMap (2010 - 2025).png" alt="Logo" width="800"> |

| NIFTY 50 HeatMap (2018 - 2025) |
|--------------------------------|
| <img src="HeatMaps Screenshots/NIFTY 50/NIFTY 50 HeatMap (2018 - 2025).png" alt="Logo" width="800"> |


- **NIFTY NEXT 50 :**

| NIFTY NEXT 50 HeatMap (2010 - 2025) |
|--------------------------------|
| <img src="HeatMaps Screenshots/NIFTY NEXT 50/NIFTY NEXT 50 HeatMap (2010 - 2025).png" alt="Logo" width="800"> |

| NIFTY NEXT 50 HeatMap (2018 - 2025) |
|--------------------------------|
| <img src="HeatMaps Screenshots/NIFTY NEXT 50/NIFTY NEXT 50 HeatMap (2018 - 2025).png" alt="Logo" width="800"> |


## Contributing  
Contributions are welcome! 🎉  

To contribute:  
1. Fork this repository.  
2. Create a new branch:  
```bash
  git checkout -b feature-new-feature
```
3. Make changes and commit:
  ```bash
  git commit -m "Added a new feature
```
4. Push to GitHub and open a Pull Request.   
