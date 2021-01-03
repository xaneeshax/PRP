

# This is an alias
import pandas as pd


dictionary = {
    
    'Shreya' : [78, 98, 87, 56, 79],
    'Aneesha' : [87, 68, 98, 90, 45],
    'Tammy' : [100, 100, 100, 99 , 98]
    
    }

df = pd.DataFrame(dictionary, index=['calculus', 'us history', 'english', 'statistics', 'biology'])


# What was the average of Shreya's grades?
df['Shreya']

# What was the average score of the calculus test?
df.T['calculus']


# Using loc
df.loc[['calculus', 'biology']]

df.loc[['calculus', 'biology'], :]

df.loc[['calculus', 'biology'], 'Aneesha']

df.loc[['calculus', 'biology'], ['Shreya', 'Aneesha']]

df.loc['calculus' : 'statistics', 'Tammy']

df.iloc[[0, 1, 3], 0]

df.iloc[0:2, 1:2]

df.at['calculus', 'Aneesha']

df.iat[0, 2]




