import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn import tree

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

names = soup.find_all("h3", {"class":"country-name"}) # scrap names of countries
capitals = soup.find_all("span", {"class":"country-capital"}) # scrap capitals
populations = soup.find_all("span", {"class":"country-population"}) # scrap populations
areas = soup.find_all("span", {"class":"country-area"}) # scrap area

connection = mysql.connector.connect(host = "127.0.0.1", user = "", password = "", database = "country_info") # connect to database
cursor = connection.cursor()

for i in range(len(names)):
    # to extract values
    name, capital, population, area = names[i].text.strip(), capitals[i].text.strip(), populations[i].text.strip(), areas[i].text.strip()
    population = int(population.replace(",", "")) # we remove these characters to prevent error in machine learning
    area = float(area.replace(",", ""))
    if "'" in name : # we replace these characters to prevent error in mysql
        name = name.replace("'", "''")
    if "'" in capital :
        capital = capital.replace("'", "''")
    # write on database
    cursor.execute(f"INSERT INTO information(Country, Capital, Population, Area) VALUES(\'{name}\', \'{capital}\', {population}, {area})")
    connection.commit()

x = []
y = []
# read from database
cursor.execute("SELECT Population, Area FROM information")
result = cursor.fetchall()
for (p, a) in result :
    x.append([p]) # This code gets the population | p is population
    y.append(a) # and then gives the area of ​​the country | a is area

clf = tree.DecisionTreeClassifier().fit(x, y) # use this to learn machine

new_data = [[1450935791], [345426571], [50448963], [24672760], [51717590]] # Enter the desired number here.
answer = clf.predict(new_data)
print(answer[0], answer[1], answer[2], answer[3]) # now you have the area

connection.close()