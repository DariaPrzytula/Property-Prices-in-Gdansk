import pandas as pd
import numpy as np

#%% 

# Import data

url="https://github.com/DariaPrzytula/Property-Prices-in-Gdansk/blob/main/raw_data.xlsx?raw=true"
df = pd.read_excel(url)

#%% 

# Organize data in the "Price" column

df['Price'] = df['Price'].str.replace('zł', '')

#%% 

# Organize data in the "District" column

df['District'] = df['District'].str.split(',').str[0]

df.replace("Gdańsk Orunia Górna", "Orunia", inplace=True)
df.replace("Gdańsk Morena ", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk", "Śródmieście", inplace=True)
df.replace("Gdańsk Łostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Zakoniczyn", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Dolne Miasto", "Śródmieście", inplace=True)
df.replace("Gdańsk Ujeścisko", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Długie Ogordy", "Śródmieście", inplace=True)
df.replace("Gdańsk Piecki Migowo/Jasień", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Św.Wojciech", "Orunia", inplace=True)
df.replace("Gdańsk Kiełpinek", "Jasień", inplace=True)
df.replace("Gdańsk Stare Przedmieście", "Śródmieście", inplace=True)
df.replace("Gdańsk Niedźwiednik", "Brętowo", inplace=True)
df.replace("Gdańsk Kowale", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Nowe Ogrody", "Śródmieście", inplace=True)
df.replace("Gdańsk Południe", "Jasień", inplace=True)
df.replace("Gdańsk Karczemki", "Kokoszki", inplace=True)
df.replace("Gdańsk Młode Miasto", "Młyńska", inplace=True)
df.replace("Gdańsk Sobieszewo", "Wyspa Sobieszewska", inplace=True)
df.replace("Gdańsk Biskupia Górka", "Śródmieście", inplace=True)
df.replace("Gdańsk Złota Karczma", "Matarnia", inplace=True)
df.replace("Gdańsk Maćkowy", "Orunia", inplace=True)
df.replace("Gdańsk Porzymorze", "Przymorze", inplace=True)
df.replace("Gdańsk młyńska", "Młyńska", inplace=True)
df.replace("Gdańsk  Chełm", "Chełm", inplace=True)
df.replace("Gdańsk Orunia", "Orunia", inplace=True)
df.replace("Gdańsk Wrzeszcz", "Wrzeszcz", inplace=True)
df.replace("Gdańsk Śródmieście", "Śródmieście", inplace=True)
df.replace("Gdańsk Żabianka", "Żabianka", inplace=True)
df.replace("Gdańsk Przymorze", "Przymorze", inplace=True)
df.replace("Gdańsk Morena", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Przeróbka", "Przeróbka", inplace=True)
df.replace("Gdańsk Jasień", "Jasień", inplace=True)
df.replace("Gdańsk Stogi", "Stogi", inplace=True)
df.replace("Gdańsk Brzeźno", "Brzeźno", inplace=True)
df.replace("Gdańsk Chełm", "Chełm", inplace=True)
df.replace("Gdańsk Strzyża", "Strzyża", inplace=True)
df.replace("Gdańsk Młyńska", "Młyńska", inplace=True)
df.replace("Gdańsk VII Dwór", "VII Dwór", inplace=True)
df.replace("Gdańsk Jelitkowo", "Jelitkowo", inplace=True)
df.replace("Gdańsk Młyniska", "Młyńska", inplace=True)
df.replace("Gdańsk Letnica", "Letnica", inplace=True)
df.replace("Gdańsk Św.Wojciech", "Orunia", inplace=True)
df.replace("Gdańsk Nowy Port", "Nowy Port", inplace=True)
df.replace("Gdańsk Rudniki", "Rudniki", inplace=True)
df.replace("Gdańsk Ujeścisko-Łostowice", "Ujeścisko-Łosotowice", inplace=True)
df.replace("Gdańsk młyniska", "Młyńska", inplace=True)
df.replace("Gdańsk Chełm", "Chełm", inplace=True)
df.replace("Gdańsk Oliwa", "Oliwa", inplace=True)
df.replace("Gdańsk Piecki-Migowo", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Suchanino", "Suchanino", inplace=True)
df.replace("Gdańsk Długie Ogrody", "Śródmieście", inplace=True)
df.replace("Gdańsk Kokoszki", "Kokoszki", inplace=True)
df.replace("Gdańsk Matarnia", "Matarnia", inplace=True)
df.replace("Gdańsk Górki Zachodnie", "Górki Zachodnie", inplace=True)
df.replace("Gdańsk Olszynka", "Olszynka", inplace=True)
df.replace("Gdańsk  Suchanino", "Suchanino", inplace=True)
df.replace("Gdańsk  Chełm", "Chełm", inplace=True)
df.replace("Gdańsk Centrum", "Śródmieście", inplace=True)
df.replace("Gdańsk Ujeścisko-Łosotowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Matarnia - Rębiechowo", "Matarnia", inplace=True)
df.replace("Gdańsk Łostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Zaspa Młyniec", "Zaspa", inplace=True)
df.replace("Gdańsk Vii Dwór", "VII Dwór", inplace=True)
df.replace("Gdański", "Śródmieście", inplace=True)
df.replace("Gdańsk Myśliwska", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Przymorze Wielkie", "Przymorze", inplace=True)
df.replace("Gdańsk Lostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Starówka", "Śródmieście", inplace=True)
df.replace("Ujeścisko-Łosotowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk  Ujeścisko Łostowice ", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Piecki Migowo", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Lostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk  Ujeścisko", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Żabaianka", "Żabianka", inplace=True)
df.replace("Gdańsk  Łostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk  Lostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Lostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk Łostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdansk Lostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk  Ujeścisko ", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdansk Łostowice", "Ujeścisko-Łostowice", inplace=True)
df.replace("Gdańsk  Chłopska 14", "Przymorze", inplace=True)
df.replace("Gdańsk Chłopska 14", "Przymorze", inplace=True)
df.replace("Gdańsk  Żabianka", "Żabianka", inplace=True)
df.replace("Gdańsk Aniołki", "Aniołki", inplace=True)
df.replace("Gdańsk Siedlce", "Siedlce", inplace=True)
df.replace("Gdańsk Św. Wojciech", "Orunia", inplace=True)
df.replace("Gdańsk Rębowo", "Jasień", inplace=True)
df.replace("Gdańsk Zaspa", "Zaspa", inplace=True)
df.replace("Gdańsk Piecki-migowo", "Piecki-Migowo", inplace=True)
df.replace("Gdańsk Chłopska", "Gdańsk Przymorze", inplace=True)
df.replace("Gdańsk Osowa", "Osowa", inplace=True)
df.replace("Gdańsk  Chełm ", "Chełm", inplace=True)
df.replace("Gdańsk Przymorze", "Przymorze", inplace=True)

#%% 

# Organize data in the "Floor" column - part1

df.replace("2009", np.nan, inplace=True)
df.replace("2019", np.nan, inplace=True)
df.replace("2017", np.nan, inplace=True)
df.replace("2022", np.nan, inplace=True)

#%% 

# Drop missing values and unused columns

df= df.dropna()
df = df.drop(columns=['Price per square meter'])

#%%

# Organize data in the "Floor" column - part2

df.replace("parter", "0", inplace=True)
df["Floor"] = df["Floor"].astype("int64")
df["Floor"] = df["Floor"] + 1

#%% 

# Change types of data

df['Year'].fillna(0, inplace=True)
df['Year'] = df['Year'].astype('int64')

#%% 

# Organize data in the "Price" column

df['Price'] = df['Price'].replace({' ':'', ',':''}, regex=True).astype('int64')
df = df.loc[(df['Price'] < 6000000)]

#%% 

# Save data to dashboard

df.to_excel('data_to_dashboard.xlsx')

#%% 

# Convert categorical variable into variables

df = pd.get_dummies(df, drop_first=True)

#%% 

# Save data to model 

df.to_csv('data_to_model.csv')

#%% 

# Prepare data to model

X = df.copy()
y = X.pop('Price')

#%% 

# Split a dataset into a training set and a test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

#%% 

# Model 

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_test, y_test)

model_score = model.score(X_test, y_test)

#%% 

# Save model

import pickle

with open('model.pickle', 'wb') as file:
    pickle.dump(model, file)

 