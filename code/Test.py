import pandas as pd

pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")

fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
q1.check()
print(fruits)

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'])
fruit_sales.index = ['2017 Sales', '2018 Sales']
q2.check()
print(fruit_sales)

#ingradients = pd.DataFrame([['Flour','4 cups'], ['Milk','1 cup'], ['Eggs','2 Large'],['Spam','1 can']], columns=['Ingradient', 'Qty'])
# ingradients.Name = 'Dinner'
ingradients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
q3.check()
print(ingradients)

# import csv 
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)
# print(wine_reviews.head())
print(wine_reviews.shape)
print(wine_reviews.columns)
print(wine_reviews.country[5])
print(wine_reviews.loc[-3:,['winery', 'country', 'points']])


# export to csv
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
# print(animals)
animals.to_csv('../input/cows_and_goats.csv')