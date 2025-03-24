🌍 Country Information Scraper & Predictor
📌 Overview
This is a beginner-friendly Python project that:
✅ Scrapes country information (name, capital, population, and area) from ScrapeThisSite.
✅ Stores the data in a MySQL database.
✅ Uses a simple Decision Tree model to predict a country's area based on its population.

This is not an exact or professional model—it's just for learning and practice! 🚀

🛠 Requirements
You'll need the following installed:

Python 3.x

MySQL database

The following Python libraries:

sh
Copy
Edit
pip install requests beautifulsoup4 mysql-connector-python scikit-learn
🔧 Setup & Usage
1️⃣ MySQL Setup
Before running the script, make sure you have a MySQL database set up. Run these commands in MySQL:

sql
Copy
Edit
CREATE DATABASE country_info;
USE country_info;
CREATE TABLE information (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Country VARCHAR(255),
    Capital VARCHAR(255),
    Population BIGINT,
    Area FLOAT
);
2️⃣ Run the Script
Once MySQL is ready, simply run:

sh
Copy
Edit
python script.py
This will:
1️⃣ Scrape country data from the website.
2️⃣ Save the data in the MySQL database.
3️⃣ Train a simple Decision Tree model.
4️⃣ Predict the area of some countries based on their population.

⚠️ Important Notes
This is not a perfect or professional model—it’s just for learning!

The Decision Tree may give incorrect or random predictions because it’s trained on a small dataset.

Special characters in country names are handled to avoid MySQL errors.

📚 Learning Goals
This project is great for beginners who want to practice:
✅ Web scraping with BeautifulSoup
✅ Storing data in MySQL with mysql-connector-python
✅ Basic machine learning with scikit-learn

📜 License
Feel free to use and modify this project for learning purposes! 😊