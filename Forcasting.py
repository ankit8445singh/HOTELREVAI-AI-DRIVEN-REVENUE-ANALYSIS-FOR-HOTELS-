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
