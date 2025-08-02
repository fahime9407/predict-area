
# 🌍 Country Info Scraper & Area Predictor

A beginner-friendly project that combines **web scraping**, **data preprocessing**, **machine learning**, and a simple **GUI app** — all in Python! You can either use live web data or fall back to a local dataset.

---

## 📦 Project Features

✅ Web scraping from [scrapethissite.com](https://www.scrapethissite.com/pages/simple/)
✅ Data cleaning & outlier removal
✅ Train a `DecisionTreeRegressor` to predict **area** based on **population**
✅ Use MySQL to store structured country data
✅ GUI app built with **Tkinter** for live predictions
✅ Ready-to-use dataset provided if scraping fails

---

## 🗂️ File Structure

| File                        | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| `main.ipynb` | Full data pipeline (scraping → cleaning → training → evaluation) + Tkinter GUI |
| `main.py`           | Scrapes + saves to MySQL + trains Regressor + launches prediction GUI         |
| `country_info.csv`          | Cleaned country dataset (use if scraping fails)                                |
| `requirements.txt`          | All required Python packages                                                   |

---

## ⚙️ Installation

1. 🔧 Clone the repo

   ```bash
   git clone https://github.com/fahime9407/predict-area.git
   cd predict-area
   ```

2. 📦 Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. 🛢️ (Optional) Setup MySQL

   * Create a database named `country_info`
   * Create a table called `information` with fields: `Country`, `Capital`, `Population`, `Area`

---

## 🚀 How to Use

### Option 1: Run the Notebook

Ideal for analysis and visualization.

```bash
jupyter notebook main.ipynb
```

You can skip scraping and use `country_info.csv` directly.

---

### Option 2: Run the Script

Ideal for testing with a database and GUI.

```bash
python main.py
```

> 💡 The GUI allows you to enter a population and see the predicted area!

---

## ❗ Notes

* All required libraries are listed in `requirements.txt`.
* If scraping fails (e.g., due to internet issues), use the provided `country_info.csv` as a backup dataset.

