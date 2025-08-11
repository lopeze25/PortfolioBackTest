# PortfolioBackTest

A Python backtesting tool for manually backtesting asset certain portfolios and computing **CAGRS** (compound annual growth rates), drawdowns, and growth.

## Features
- Pulls S&P 500 prices via `yfinance`
- Pulls 3-month T-Bill (DTB3) and 5-year Treasury (DGS5) from FRED via `pandas-datareader`
- Optional Gold input from CSV
- Compares a dynamic UPRO/T-Bill timing model vs a static SSO/ZROZ/Gold mix
- Outputs CAGR, max drawdown, and growth-of-$1,000 chart

In this case I was trying to find the effectiveness of gold one of my portfolios (SSO/ZROZ/GLD) and the CAGR. 

## Requirements
```bash
pip install yfinance pandas pandas_datareader matplotlib numpy


