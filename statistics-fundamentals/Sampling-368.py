## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
#print(wnba.head())
#print(wnba.tail())
#print(wnba.shape)
parameter = wnba["Games Played"].max()
print(parameter)
sample = wnba.sample(30, random_state=1)["Games Played"].max()
print(sample)
sampling_error = abs(sample - parameter)

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt
mean_wnba = []
num = []
wnba = pd.read_csv('wnba.csv')
for i in range(0,100):
    mean_wnba.append(wnba["PTS"].sample(10, random_state=i).mean())
    num.append(i+1)
print(num)
plt.scatter(num, mean_wnba)
plt.axhline(y=wnba["PTS"].mean())