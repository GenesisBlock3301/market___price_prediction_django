import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import itertools

df=pd.read_csv('Pattern_Recognised_var02.csv')
next_data=[]

for i in range(0,len(df['Pattern'])):
    try:
        if df['Pattern'][i]==res:
            next_data.append(df['Pattern'][i+1])
    except:
        pass
count=[]
for i in next_data:
    cn=0
    for j in next_data:
        if i==j:
            cn=cn+1
    count.append(cn)
len(count)
len(next_data)

du=pd.DataFrame()

du['next_pattern']=next_data
du['Frequency']=count
probability_of_apperaing=[]
for i in du['Frequency']:
    probability_of_apperaing.append((float(i)/len(next_data))*100)

du['probability_of_apperaing']=probability_of_apperaing