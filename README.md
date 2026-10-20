# HOTELREVAI

AI-Driven Revenue Analysis for Hotels

A smart hotel analytics and forecasting project that combines business intelligence, data cleaning, revenue analysis, and predictive modeling to help hotel managers improve occupancy, pricing, and profitability.

## Overview

HOTELREVAI is designed to analyze hotel booking data, identify patterns in guest behavior, and forecast future revenue and occupancy using Python and Power BI. It helps hotels understand their performance across key dimensions such as room type, booking source, guest segment, and time trends.

The project focuses on:
- Revenue optimization
- Occupancy analysis
- Forecasting cancellations and demand
- Guest segmentation
- Business dashboards and KPI tracking

## Problem Statement

Hotels often struggle to understand how booking trends, pricing strategies, seasonality, and cancellation patterns impact revenue. Without clear visibility into operational data, decisions around promotions, inventory management, and pricing remain reactive rather than proactive.

HOTELREVAI addresses this by turning booking data into actionable insights and predictive intelligence.

## Key Features

- Interactive Power BI dashboard for hotel performance monitoring
- Revenue, occupancy, and ADR analysis
- Booking trend and seasonality analysis
- AI-based forecasting using Facebook Prophet
- Guest segmentation for targeted marketing
- Cancellation and lead-time analysis
- Data cleaning and transformation for reliable analytics

## Tech Stack

| Area | Tools |
|------|-------|
| BI & Dashboards | Power BI |
| Data Cleaning | Power Query, Pandas |
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Forecasting | Facebook Prophet |
| Visualization | Matplotlib, Streamlit |
| App UI | Streamlit |

## Dataset

The project uses hotel booking data stored in:

- `hotel_data.csv`

The dataset includes information such as:
- Booking ID
- Customer ID
- Room type
- Reservation dates
- Booking source
- Payment and revenue details
- Cancellation indicators

The data is processed for:
- Missing value handling
- Duplicate removal
- Type conversion
- Aggregation and time-based analysis

## Data Model

The solution follows a star schema design for analytical reporting:

- Fact table: `Fact_Bookings`
- Dimension tables: Guests, Rooms, Hotels, Dates, Booking Source
- Relationships: one-to-many to maintain data integrity and reporting consistency

## KPIs Tracked

- Occupancy Rate
- ADR (Average Daily Rate)
- RevPAR (Revenue per Available Room)
- Booking Duration
- Revenue Trends
- Cancellation Rate
- Demand Forecasts

## Forecasting Module

The forecasting logic is implemented in `Forcasting.py` and uses Prophet to predict:

- Revenue
- Cancellations
- Occupancy trends

It groups booking data by reservation date, trains a time-series model, and creates future demand forecasts for the next 90 days.

## Repository Structure

```text
HOTELREVAI/
├── README.md
├── hotel_data.csv
├── Forcasting.py
├── requirement.txt
├── HOTEL REVENUE POWERBI(2,3,5).pbix
├── HOTEL_REVENUE_POWER-BI(4).pbix
├── HOTEL BOOKING REVENUE .pptx
├── 2-Hotel Business Understand and Improve Revenue.pdf
├── LICENSE
└── .gitignore (if added later)
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ankit8445singh/HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-.git
cd HOTELREVAI-AI-DRIVEN-REVENUE-ANALYSIS-FOR-HOTELS-
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows:
```bash
venv\Scripts\activate
```

- macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

If you want to install manually:

```bash
pip install streamlit pandas prophet matplotlib scikit-learn pystan
```

### 4. Run the forecasting script

```bash
python Forcasting.py
```

### 5. Run the Streamlit app (if integrated later)

```bash
streamlit run hotel_deshboard.py
```

## Example Workflow

1. Load hotel booking data
2. Clean and validate the dataset
3. Aggregate metrics by day and room type
4. Build business dashboards in Power BI
5. Run forecasting models for revenue and occupancy
6. Use insights to improve pricing and guest strategy

## Business Impact

This project helps hotels:
- Improve pricing decisions
- Identify demand fluctuations
- Reduce cancellations
- Improve marketing targeting
- Increase operational efficiency
- Support better revenue management strategy

## Project Milestones

- Milestone 1: Data cleaning and schema design
- Milestone 2: Power BI dashboard creation
- Milestone 3: Guest segmentation and persona analysis
- Milestone 4: Forecasting model development
- Milestone 5: Integrated business intelligence solution

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Ankit Singh

## Notes

This project combines analytical modeling with business intelligence and is suitable for academic, internship, or portfolio demonstration purposes in the domain of hotel revenue analytics.

---

If you want, I can also create a more polished version tailored for GitHub with:
- project screenshots section
- badges
- architecture diagram
- a short demo image banner
- a more professional portfolio-style README
