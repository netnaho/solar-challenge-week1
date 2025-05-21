import pandas as pd
import streamlit as st

@st.cache_data
def load_data(country: str) -> pd.DataFrame:
    """
    Load the cleaned CSV for a given country.
    Expects files named <country>_clean.csv in ../data/.
    """
    path = f"./data/{country.lower().replace(' ', '_')}_clean.csv"
    df = pd.read_csv(path, parse_dates=['Timestamp       '])
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
    df["Region"] = country
    return df

def get_summary_table(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    """
    Returns mean, median, std for the specified metric, grouped by Region.
    """
    summary = (
        df.groupby('Region')[metric]
          .agg(['mean', 'median', 'std'])
          .round(2)
          .reset_index()
    )
    return summary
