#!/usr/bin/env python
# coding: utf-8

# ## Regression

# In[8]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from tkinter import *
from tkinter import ttk


# ### Dataset Definition

# In[9]:


# first of all we should send a HTTP request to the server.
try:
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
except:
    print("Error!")


# In[10]:


# then we should extract needed information from the HTML file.
soup = BeautifulSoup(response.text, "html.parser")

names = soup.find_all("h3", {"class": "country-name"})
populations = soup.find_all("span", {"class": "country-population"})
areas = soup.find_all("span", {"class": "country-area"})

for i in range(len(names)):
    names[i] = str(names[i].text.strip())
    populations[i] = int(populations[i].text.strip())
    areas[i] = float(areas[i].text.strip())


# In[11]:


# now we create a data frame for the extracted information.
info = {
    "name": names,
    "population": populations,
    "area": areas
}
df = pd.DataFrame(info)
df.to_csv("country_info")

df.head()


# ### Preprocessing

# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


plt.scatter(df["population"], df["area"], color="green")
plt.xlabel("population".title())
plt.ylabel("area".title())
plt.show()


# In[15]:


# We will now remove the outlier data points on "population" column.
Q3 = df["population"].quantile(0.75)
IQR = Q3
upper_bound = Q3 + 1.5 * IQR

df["population"] = df["population"].where(df["population"] < upper_bound, np.nan)

df = df.dropna()
df.info()


# In[16]:


plt.scatter(df["population"], df["area"], color="red")
plt.xlabel("population".title())
plt.ylabel("area".title())
plt.show()


# In[17]:


# We will now remove the outlier data points on "area" column.
Q3 = df["area"].quantile(0.75)
IQR = Q3

upper_bound = Q3 + 1.5 * IQR

df["area"] = df["area"].where(df["area"] < upper_bound, np.nan)

df = df.dropna()
df.info()


# In[18]:


plt.scatter(df["population"], df["area"], color="blue")
plt.xlabel("population".title())
plt.ylabel("area".title())
plt.show()


# In[19]:


# split data to train and test
msk = np.random.rand(len(df)) < 0.8

train, test = df[msk], df[~msk]

train.shape, test.shape


# ### Model Definition

# In[20]:


mymodel = DecisionTreeRegressor(max_depth=4)

x_train = np.asanyarray(train[["population"]])
y_train = np.asanyarray(train[["area"]])

mymodel.fit(x_train, y_train.ravel())


# ### Model Evaluation

# In[21]:


x_test = np.asanyarray(test[["population"]])
y_test = np.asanyarray(test[["area"]])

y_pred = mymodel.predict(x_test)


# In[22]:


# The R2 score is quite low, indicating that the model has very low accuracy
mse = np.mean((y_test - y_pred) ** 2)
mae = np.mean(np.absolute(y_test - y_pred))
r2 = r2_score(y_test, y_pred)

print(f"mean squared error : {mse:.5f} | mean absolute error : {mae:.5f} | r2 score : {r2:.5f}")


# In[23]:


def predict_area():
    x = int(entry.get())
    y = mymodel.predict([[x]])
    label_result.config(text=f"our prediction : {y[0]:.5f}")

root = Tk()
root.title("Area Predictor")
frm = ttk.Frame(root, padding=10) # Padding specifies the space between the widget and outer edges.
frm.grid()
label_1 = ttk.Label(frm, text="population : ").grid(row=0, column=0, pady=(0, 10))
entry = ttk.Entry(frm)
entry.grid(row=0, column=1, pady=(0, 10)) # The pady parameter defines the vertical spacing between rows
ttk.Button(frm, text="Predict", width=40, command=predict_area).grid(row=1, column=1)
label_result = ttk.Label(frm, text="our prediction ... ")
label_result.grid(row=2, column=0, pady=(0, 10))
ttk.Button(frm, text="Done",width=40, command=root.destroy).grid(row=3, column=1)
root.mainloop()


# In[ ]:




