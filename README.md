
# Country Information Scraper & Area Predictor

A Python project that:
1. Scrapes country data (name, capital, population, and area) from a public website.
2. Stores the data in a MySQL database.
3. Trains a Decision Tree regression model to predict the **area** of a country based on its **population**.
4. Provides a **Tkinter-based GUI** for prediction and accuracy display.

---

## 📌 Features
- **Web Scraping** using `requests` and `BeautifulSoup`
- **Data Storage** in MySQL
- **Machine Learning Model** with `DecisionTreeRegressor` from `scikit-learn`
- **Accuracy Calculation** using R² score
- **GUI Application** for real-time prediction

---

## 🛠️ Requirements
Make sure you have Python 3.x installed and the following libraries:

You can install all required packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
````

The main dependencies are:

* `requests`
* `beautifulsoup4`
* `mysql-connector-python`
* `scikit-learn`
* `numpy`
* `tkinter` (usually comes pre-installed with Python)

You will also need:

* **MySQL Server** installed and running.
* A database named `country_info` with a table:

```sql
CREATE TABLE information (
    Country VARCHAR(255),
    Capital VARCHAR(255),
    Population BIGINT,
    Area FLOAT
);
```

---

## Alternative Data Source

If working with MySQL is difficult for you, a CSV file containing the scraped country data is also included in this repository.
You can use this file to load the data without needing a database setup.

---

## ⚙️ How It Works

1. **Scraping**

   * Fetches country data from:
     `https://www.scrapethissite.com/pages/simple/`
   * Extracts **name**, **capital**, **population**, and **area**.

2. **Database Storage**

   * Inserts the scraped data into the `information` table of the `country_info` MySQL database.

3. **Model Training**

   * Reads population and area from the database.
   * Fits a Decision Tree Regressor model.

4. **GUI Prediction**

   * First GUI: Displays model accuracy.
   * Second GUI: Takes **population** as input and predicts **area**.

---

## 🚀 Usage

1. **Configure Database Connection**
   In the code:

   ```python
   connection = mysql.connector.connect(
       host="127.0.0.1",
       user="root",
       password="YOUR_PASSWORD",
       database="country_info"
   )
   ```

   Replace `YOUR_PASSWORD` with your MySQL password.

2. **Run the Script**

   ```bash
   python main.py
   ```

3. **Interact with the GUI**

   * First window: Shows model accuracy. Click **OK**.
   * Second window: Enter population, click **Predict**, and view predicted area.

---

## 🔒 Security Notes

* **Do NOT** commit your real MySQL password to GitHub. Use environment variables or a `.env` file.
* The provided scraping URL is for demonstration purposes only. Ensure you respect website `robots.txt` rules when scraping.

---

## 📷 Screenshot Example

![GUI Screenshot](image.png)

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.
