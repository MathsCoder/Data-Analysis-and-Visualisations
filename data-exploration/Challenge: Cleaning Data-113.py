## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
print(avengers.head(5))

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame(avengers[avengers["Year"] >= 1960])

avengers['Year'].hist()

## 5. Consolidating Deaths ##

def deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if death == 'YES':
            num_deaths += 1
        else:
            continue
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(deaths, axis=1)

## 6. Verifying Years Since Joining ##

import numpy as np
joined_accuracy_count  = int()
#if ( true_avengers["Years since joining"] == (2015 - true_avengers["Year"]) ):
 #   joined_accuracy_count +=1
#print(true_avengers["Years since joining"])
#print(2015 - true_avengers["Year"])
joined_accuracy_count = np.sum( true_avengers["Years since joining"] == (2015 - true_avengers["Year"]) ) 