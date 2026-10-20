# HOTELREVAI

AI-Driven Revenue Analysis for Hotels

HOTELREVAI is an AI-powered business intelligence project designed to analyze hotel booking data, forecast demand, and improve revenue decision-making. The project combines Python-based forecasting with Power BI dashboards to help hotel teams understand occupancy, pricing, cancellations, and revenue performance.

## Overview

This project focuses on turning hotel booking data into actionable insights. By cleaning the raw dataset, aggregating key metrics, and applying time-series forecasting models, the solution helps hotels identify trends, optimize room pricing, and improve planning.

The core forecasting logic is implemented in `Forcasting.py`, which includes functions for:
- `load_data()`
- `get_summary()`
- `forecast_revenue()`
- `forecast_cancellations()`
- `forecast_occupancy()`

## Features

- Revenue trend analysis
- Occupancy forecasting
- Cancellation prediction
- Booking-level KPI summaries
- Power BI visual analytics
- AI-driven forecasting using Prophet
- Data cleaning and preprocessing for hotel data

## Tech Stack

- Python
- Pandas
- NumPy
- Facebook Prophet
- Matplotlib
- Power BI
- Streamlit

## Dataset

The project uses hotel booking data stored in `hotel_data.csv`.

The data includes fields such as:
- Booking ID
- Customer ID
- Reservation dates
- Room type
- Payment values
- ADR
- Cancellation status

## Forecasting Module

The forecasting module uses Prophet to generate predictions for future values based on time-series trends.

```python
import pandas as pd
from prophet import Prophet

def load_data(file_path="../data/hotel_data.csv"):
    df = pd.read_csv(file_path, parse_dates=["reservation_status_date"], dayfirst=True)
    return df

def get_summary(df):
    summary = {
        "Total Bookings": len(df),
        "Total Revenue": df["total_payment"].sum(),
        "Avg ADR": round(df["adr"].mean(), 2),
        "Cancellations": df["canceled"].sum()
    }
    return summary

def forecast_revenue(df, periods=90):
    data = df.groupby("reservation_status_date")["total_payment"].sum().reset_index()
    data.columns = ["ds", "y"]

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def forecast_cancellations(df, periods=90):
    data = df.groupby("reservation_status_date")["canceled"].sum().reset_index()
    data.columns = ["ds", "y"]

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def forecast_occupancy(df, periods=90):
    df["reservation_status_date"] = pd.to_datetime(
        df["reservation_status_date"], dayfirst=True, errors="coerce"
    )
    df_clean = df.dropna(subset=["customer_ID", "reservation_status_date"])
    
    if df_clean.empty:
        return pd.DataFrame()
    
    data = df_clean.groupby("reservation_status_date")["customer_ID"].count().reset_index()
    data.columns = ["ds", "y"]
    
    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
```

## Project Structure

```text
HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-
├── README.md
├── Forcasting.py
├── hotel_data.csv
├── requirement.txt
├── HOTEL REVENUE POWERBI(2,3,5).pbix
├── HOTEL_REVENUE_POWER-BI(4).pbix
├── HOTEL BOOKING REVENUE .pptx
├── 2-Hotel Business Understand and Improve Revenue.pdf
├── LICENSE
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ankit8445singh/HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-.git
cd HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirement.txt
```

## How to Run

Run the forecasting script:

```bash
python Forcasting.py
```

If you are using a Streamlit interface later, you can run:

```bash
streamlit run hotel_deshboard.py
```

## Business Impact

This project helps hotel managers:
- Forecast future occupancy and revenue
- Understand seasonal demand shifts
- Analyze cancellation trends
- Improve pricing decisions
- Support smarter revenue management

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Ankit Singh
