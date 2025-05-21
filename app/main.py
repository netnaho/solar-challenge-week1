import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from utils import load_data, get_summary_table

st.set_page_config(
    page_title="Solar Potential Dashboard",
    layout="wide"
)

st.title("🌞 MoonLight Energy Solutions — Solar Potential Explorer")

# --- Sidebar Widgets ---
st.sidebar.header("Controls")
countries = ['Benin', 'SierraLeone', 'Togo']
selected_countries = st.sidebar.multiselect(
    "Select countries to compare:",
    options=countries,
    default=countries
)

metric = st.sidebar.selectbox(
    "Metric to visualize:",
    options=['GHI', 'DNI', 'DHI']
)

# --- Load & concatenate data ---
dfs = [load_data(c) for c in selected_countries]
df = pd.concat(dfs, ignore_index=True)

# --- Boxplot of selected metric ---
st.subheader(f"📦 {metric} Distribution by Region")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x='Region', y=metric, ax=ax)
ax.set_xlabel("")
ax.set_ylabel(f"{metric} (W/m²)")
st.pyplot(fig)

# --- Top Regions Table ---
st.subheader(f"🏆 Top Regions by Average {metric}")
summary = get_summary_table(df, metric)
summary = summary.sort_values('mean', ascending=False).reset_index(drop=True)
st.dataframe(summary)

# --- Optional: Time Series Viewer ---
if st.checkbox("Show time-series trends"):
    st.subheader(f"⏱️ {metric} Over Time")
    fig_ts, ax_ts = plt.subplots(figsize=(10, 4))
    for region in selected_countries:
        sub = df[df['Region'] == region]
        sub = sub.set_index('Timestamp').resample('D')[metric].mean()
        ax_ts.plot(sub.index, sub.values, label=region)
    ax_ts.legend()
    ax_ts.set_ylabel(f"{metric} (daily mean)")
    st.pyplot(fig_ts)
