# Country Information Scraper & Predictor  

## Overview  
This Python program scrapes country data (name, capital, population, and area) from [ScrapeThisSite](https://www.scrapethissite.com/pages/simple/), stores it in a MySQL database, and uses a Decision Tree classifier from `scikit-learn` to predict the area of countries based on their population.  

## Features  
- **Web Scraping**: Extracts country details from a website using `requests` and `BeautifulSoup`.  
- **Database Storage**: Saves the data in a MySQL database for persistent storage.  
- **Machine Learning Prediction**: Uses a Decision Tree classifier to predict a country's area based on population.  

## Requirements  
Ensure you have the following installed before running the program:  
- Python 3.x  
- `requests`  
- `BeautifulSoup4`  
- `mysql-connector-python`  
- `scikit-learn`  
- MySQL database (with a table for storing country data)  

## Installation  

1. Install required Python libraries:  
   ```sh
   pip install requests beautifulsoup4 mysql-connector-python scikit-learn
   ```  
2. Set up a MySQL database and create a table:  
   ```sql
   CREATE DATABASE country_info;
   USE country_info;
   CREATE TABLE information (
       id INT AUTO_INCREMENT PRIMARY KEY,
       Country VARCHAR(255),
       Capital VARCHAR(255),
       Population BIGINT,
       Area FLOAT
   );
   ```  
3. Update the script with your MySQL credentials if needed.  

## Usage  
Run the script using:  
```sh
python script.py
```  
It will:  
1. Scrape country data.  
2. Store the data in MySQL.  
3. Train a Decision Tree model.  
4. Predict the area for a set of given population values.  

## Notes  
- The script automatically replaces special characters in country and capital names to prevent database errors.  
- The model is trained on scraped data, so accuracy depends on the dataset size and quality.  

## License  
This project is open-source. Feel free to modify and enhance it!  

---

Let me know if you need any modifications! 🚀