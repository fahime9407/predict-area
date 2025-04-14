import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn import tree
from tkinter import *
from tkinter import ttk

# This function predicts the area based on the population input from a user interface. 
def predict_area():
    try :
        population = int(entry.get())
        answer = clf.predict([[population]])
        result_label.config(text= f"area : {answer}")
    except ValueError :
        result_label.config(text= "invalid value")

# This code sends a HTML request to specified URL and parses it using BeautifulSoup for further web scraping.
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# This code scrapes the names, capitals, populations, and areas of countries using Beautiful Soup.
names = soup.find_all("h3", {"class":"country-name"})
capitals = soup.find_all("span", {"class":"country-capital"})
populations = soup.find_all("span", {"class":"country-population"})
areas = soup.find_all("span", {"class":"country-area"})
# connect to database
connection = mysql.connector.connect(host = "127.0.0.1", user = "", password = "", database = "country_info")
cursor = connection.cursor()

# This script processes the data to ensure it is in the correct format, and inserts the cleaned data into a MySQL database.
for i in range(len(names)):
    name, capital, population, area = names[i].text.strip(), capitals[i].text.strip(), populations[i].text.strip(), areas[i].text.strip()
    population = int(population.replace(",", ""))
    area = float(area.replace(",", ""))
    if "'" in name :
        name = name.replace("'", "''")
    if "'" in capital :
        capital = capital.replace("'", "''")
    
    cursor.execute(f"INSERT INTO information(Country, Capital, Population, Area) VALUES(\'{name}\', \'{capital}\', {population}, {area})")
connection.commit()

x = []
y = []
# This code reads population and area data from a database and stores the population in a list 'x' and the area in a list 'y'.
cursor.execute("SELECT Population, Area FROM information")
result = cursor.fetchall()
for (p, a) in result :
    x.append([p])
    y.append(a)

# This code initializes a Decision Tree Classifier and fits it to the provided feature set (x) and target labels (y).
clf = tree.DecisionTreeClassifier().fit(x, y)

# This code creates a simple GUI application using Tkinter for predicting an area based on population input. 
root = Tk()
root.title("predictor")
frm = ttk.Frame(root, padding= 10)
frm.grid()
label_1 = ttk.Label(frm, text= "population : ").grid(column= 0, row= 0)
entry = ttk.Entry(frm)
entry.grid(row= 0, column= 1)
ttk.Button(frm, text= "predict", command= predict_area).grid(row= 1, column= 2)
result_label = ttk.Label(frm, text= "result : ", font=("Helvetica", 11))
result_label.grid(row= 3, column= 0)
ttk.Button(frm, text= "Done", command= root.destroy, width= 20).grid(row= 4, column= 1)
root.mainloop()

connection.close()