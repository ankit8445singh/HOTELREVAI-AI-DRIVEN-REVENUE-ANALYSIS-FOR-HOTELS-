# HOTELREVAI

AI-Driven Revenue Analysis for Hotels

HOTELREVAI is an AI-powered business intelligence project built to analyze hotel booking data, track performance metrics, and forecast future occupancy and revenue. It combines data preprocessing, hotel analytics, and predictive modeling to support better revenue management decisions.

## Overview

The project is designed to help hotel managers understand how booking behavior, room demand, cancellations, and price changes affect business performance. By analyzing hotel datasets and applying forecasting techniques, it turns raw transactional data into meaningful insights for pricing, planning, and decision-making.

This solution focuses on:
- Revenue analysis and reporting
- Occupancy trend analysis
- Cancellation forecasting
- Business KPI tracking
- Power BI-driven dashboard insights
- AI-based demand prediction

## Key Features

- AI-powered forecasting using Prophet
- Revenue and occupancy trend analysis
- Cancellation prediction for future planning
- Booking dataset cleaning and preprocessing
- KPI summaries for hotel performance
- Business intelligence dashboards in Power BI
- Actionable insights for pricing and demand management

## Tech Stack

- Python
- Pandas
- NumPy
- Prophet
- Matplotlib
- Power BI
- Streamlit

## Dataset

The project uses hotel booking data stored in the repository as hotel_data.csv.

The dataset includes booking-related information such as:
- Booking ID
- Customer ID
- Reservation dates
- Room type
- Payment and revenue information
- ADR values
- Cancellation status

## Forecasting Module

The forecasting logic is implemented in Forcasting.py and includes functions to:
- load the dataset
- summarize booking metrics
- forecast revenue
- forecast cancellations
- forecast occupancy

The model uses time-series forecasting to estimate future values based on past trends.

## Project Structure

- README.md
- Forcasting.py
- hotel_data.csv
- requirement.txt
- HOTEL REVENUE POWERBI(2,3,5).pbix
- HOTEL_REVENUE_POWER-BI(4).pbix
- HOTEL BOOKING REVENUE .pptx
- 2-Hotel Business Understand and Improve Revenue.pdf
- LICENSE

## Installation

Clone the repository:

git clone https://github.com/ankit8445singh/HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-.git
cd HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-

Create a virtual environment:

python -m venv venv

Activate the environment:

- Windows: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate

Install dependencies:

pip install -r requirement.txt

## Run the Project

Run the forecasting script:

python Forcasting.py

If you later integrate a Streamlit dashboard, it can be started with:

streamlit run hotel_deshboard.py

## Business Impact

This project helps hotels:
- improve pricing strategies
- forecast demand more accurately
- analyze booking and occupancy trends
- detect cancellation patterns early
- support better revenue management decisions

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Ankit Singh
