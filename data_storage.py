# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:16 2024

@author: DELL
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas 
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 = 25
B11 = 39

age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

"""
[30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
"""

print(age[0])
print(age[1])
print(min(age))
print(max(age))
print(len(age))
 
avg = sum(age)/len(age)
print(avg)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(gender[0:5])

print(country[3:6])

age.append(55)
print(age)
age.remove(55)
print(age)

age.insert(1,12)
print(age)
age.remove(12)
print(age)

"""
Dictionaries  - key:value pairs

cat: "a cute animal"

-unordered

"""

mammals = {'cat':'a cute animal', 'lion':'King ofthe jungle', 'elephant':'a gigantic herbivore'}
print(mammals['cat'])

"""
Data frames
"""

fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes': size_nm
    }

"""
df = DataFrame
"""

df = pandas.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df.describe())

print(df[df['sizes'] > 10])

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns = ['sizes'], inplace = True)
print(df)
