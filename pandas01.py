# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:52:08 2024

@author: DELL
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
"""

print(file.describe())

"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""

file01 = pandas.read_csv("diab_data.csv")
print(file01)
print(file01.info())
print(file01.describe())

column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",]
file02 = pandas.read_csv("housing_data.csv", names = column_names)
print(file02)
print(file02.info())
print(file02.describe())

file03 = pandas.read_csv("insurance_data.csv",skiprows = 5)
print(file03)

"""
      X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5

[63 rows x 2 columns]
"""
print(file03.info())
print(file03.describe())

"""
                X           Y
count   63.000000   63.000000
mean    22.904762   98.187302
std     23.351946   87.327553
min      0.000000    0.000000
25%      7.500000   38.850000
50%     14.000000   73.400000
75%     29.000000  140.000000
max    124.000000  422.200000
"""

file04 = pandas.read_csv("iris.csv")
print(file04)
print(file04.info())
print(file04.describe())

"""
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
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

print(B1)
print(B2)

age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)
print(age[0])
print(age[1])
print(age[10])
print(age[11])

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])


