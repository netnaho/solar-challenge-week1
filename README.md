# Solar Challenge Week 1

## Project Overview

This project provides a data analysis and visualization toolkit for comparing solar irradiance metrics—Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI)—across three West African countries: **Benin**, **Sierra Leone**, and **Togo**.

**Components:**
- Jupyter notebooks for data analysis and statistics.
- An interactive Streamlit dashboard for exploring solar potential.

---

## Features

- **Data Cleaning & Aggregation:** Loads, cleans, and merges solar irradiance data for all countries.
- **Statistical Tests:** Performs ANOVA and Kruskal-Wallis tests to compare countries.
- **Visualizations:** Boxplots, bar charts, and summary tables for solar metrics.
- **Dashboard:** Interactive Streamlit app for comparing metrics by country and region.

---

## Reproduction Steps

To set up the project and reproduce the analysis:

1. **Clone the repository**
    ```sh
    git clone git@github.com:netnaho/solar-challenge-week1.git
    cd solar-challenge-week1
    ```

2. **(Recommended) Create and activate a Python virtual environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit dashboard**
    ```sh
    streamlit run app/main.py
    ```

5. **(Optional) Run the analysis notebooks**
    ```sh
    jupyter notebook
    ```
    Then open and run `notebooks/compare_countries.ipynb`.

---

## Directory Structure

- `app/` — Streamlit dashboard app (`main.py`)
- `notebooks/` — Data analysis and visualization notebooks
- `data/` — (Expected) Cleaned CSVs for each country
- `requirements.txt` — All Python dependencies

---

## How It Works

1. **Data Loading**
   - Reads cleaned CSV files for Benin, Sierra Leone, and Togo.
   - Ensures consistent formatting and adds a "Country" column.

2. **Statistical Summary**
   - Calculates mean, median, and standard deviation of GHI, DNI, DHI per country.

3. **Statistical Testing**
   - Uses one-way ANOVA and Kruskal-Wallis tests to check for significant differences.
   - Example:
     ```python
     from scipy.stats import f_oneway, kruskal
     f_stat, p_val = f_oneway(benin["GHI"].dropna(), sierra_leone["GHI"].dropna(), togo["GHI"].dropna())
     kw_stat, kw_pval = kruskal(benin["GHI"].dropna(), sierra_leone["GHI"].dropna(), togo["GHI"].dropna())
     ```

4. **Visualization**
   - Boxplots and bar charts summarize and compare solar metrics across countries.

5. **Dashboard**
   - Lets users select countries and metrics for comparison.
   - Visualizes distributions and regional differences interactively.

---

## Key Observations

- **Benin**: Highest average and median GHI; strong solar potential.
- **Sierra Leone**: Greatest variability in GHI.
- **Togo**: Lowest solar metrics, less favorable for solar.

---

## Requirements

- Python 3.9+
- All dependencies listed in `requirements.txt` (notably: pandas, matplotlib, seaborn, streamlit, scipy, jupyter)

---

## Contributing

Feel free to fork, improve, or suggest new features and analyses via pull requests.

---

## License

[MIT License](LICENSE) (or your preferred license)
