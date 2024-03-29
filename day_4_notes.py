# -*- coding: utf-8 -*-
"""Day 4 Notes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nJoC055wXOjAUz-guePOPPs4lPkZUVk4

# Day 4

# Data Wrangling
"""

import pandas as pd
pd.set_option('precision', 2)
pd.set_option('display.max_columns', None)

"""### Add a Header"""

# Add header = None when there is no header in csv file
data = pd.read_csv('you.csv', header = None)

data

# Practice with the Avengers Data
# read the CSV
avengers = pd.read_csv('characters.csv', header=None)

avengers

"""### Rename a column"""

data

data.columns

# Rename the columns
data = data.rename(columns = {0 : 'Name', 1 : 'First Appearance',
                              2 : 'Kills', 3 : 'Profession'})

data

# Practice with the Avengers Data
# Change Name, Alignment, Intelligence, Combat

avengers = avengers.rename(columns={0 : "Name", 1 : "Alignment", 2: "Intelligence", 3: "Combat"})

avengers

"""### Setting an Index"""

data

# set a column as the index of the dataframe
data = data.set_index('Name')

data

"""### Accessing a column"""

# Access a row
data.loc['Jason']

# Accesss a row
data.loc['Peter']

# Practice with the Avengers Data
# Access any superhero character data

avengers.head(5)

avengers = avengers.set_index('Name')

avengers.loc['Black Widow']

# Specify a row and index
data.loc['Peter', 'Profession']

# Practice with the Avengers Data
# Access Hulk's "Combat" score

"""### Vector Addition"""

data

data['Kills']

# Uses vector addition to add a new column
data['Score'] = (data['First Appearance'] + data['Kills']) / 2

# Practice with the Avengers Data
# Create a Column that takes the average of both the "Intelligence" and "Combat" scores

avengers.head(5)

avengers['Average Score'] = (avengers['Intelligence'] + avengers['Combat']) / 2

"""### Unique Values"""

data

# Unique values in the column
# Returns a List
print(data['First Appearance'].unique())

avengers.head()

# Practice with the Avengers Data
# Create a Column that gets the unique "Alignment" values
avengers['Alignment'].unique()

"""### Sorting Values"""

data

# axis = 0 is for the rows
# axis = 1 is for the columns
# ascending is reversing the direction it is ordered
data = data.sort_index(axis = 1, ascending = True)
data = data.sort_index(axis = 0, ascending = True)

# You can list the data set using multiple factors
# Inplace means that the changes are assigned to the dataframe
# without having to equate the values to the data
# ex: data = data.somthing...
data.sort_values(by = ['First Appearance', 'Kills'], ascending = False, inplace = True)

avengers.head()

# Practice with the Avengers Data
# Sort values by Intelligence and Combat
avengers.sort_values(by=['Average Score'], ascending=False)

"""### Boolean Indexing"""

data

# Called Boolean Indexing
# Allows us to query a dataframe
# Is a series object
print(data['Kills'] > 1)

# The where keyword argument is used for boolean indexing
dangerous = data.where(data['Kills'] >= 2)

dangerous

"""### Drop null values"""

# Drop null values
dangerous.dropna(inplace = True)

dangerous

"""### Bitwise Operators"""

dangerous = data[data['Kills'] >= 2]

dangerous

# and in python: &
# or in python: |

# & to combine multiple conditions
# | to use a bitwise OR
dangerous = data[(data['Kills'] >= 2) & (data['First Appearance'] == 2)]

avengers.head()

# Practice with the Avengers Data
# Get all characters who have both a combat score and intelligence score of 100

avengers100 = avengers[(avengers['Combat'] >= 85) & (avengers['Intelligence'] >= 85)]

avengers100

"""### Average for a Column"""

data

data['Kills'].describe()

# Average for a column
print(data['Kills'].mean())

# Practice with the Avengers Data
# Get the average combat score
avengers['Combat'].mean()

"""### Column Indexes"""

data

# columns we would like to keep using
columns_wanted = ['Kills', 'Profession']
new_data = data[columns_wanted]

data['Score']

new_data

data

# Resets the column indexes so the names are 0,1,2...
data = data.reset_index()

data

# Practice with the Avengers Data
# Create a dataframe that only has the name and the combined score
avengers = avengers.reset_index()
avengers[['Name', 'Average Score']].sort_values('Average Score', ascending=False)

"""### Indexes"""

# Set the indexes of our dataframe using multiple attributes
# Generally make one over-arch the other
data = data.set_index(['First Appearance', 'Kills']).sort_index()

# Returns all the indexes as tuples
# Will list all even if redundant - need to use 'unique' if
# you want the unique indices
print(data.index, end = '\n\n')

# You can also choose the first index and another column
print(data.loc[1, 'Score'].mean())

# Practice with the Avengers Data
# Index data into alignment and name
# Print out teh indexes
# Find the mean of the intelligence score for all three categories

"""# Dataframe Aggregations

### Group By
"""

import pandas as pd
pd.set_option('precision', 2)
pd.set_option('display.max_columns', None)

df = pd.read_csv('divergent.csv')
df

df['original'] = ['y', 'n', 'y', 'n' , 'n', 'y', 'n' , 'n', 'n', 'y']
df

#df = df.set_index(['faction', 'name'])
df = df.set_index(['faction', 'name']).sort_index()

df.loc['dauntless'].mean()

df.groupby('faction')['brave'].mean()

# Practice with the Avengers Data
# Find the mean of the intelligence score for all three categories

df.groupby(level = 'faction').mean()

df.groupby(['faction', 'original']).mean()

df.groupby(['faction', 'original']).agg(['count', 'mean', 'std'])

# Practice with the Avengers Data
# Find the count, mean, std of the intelligence score for all three categories

def score(score):

    if score.mean() > 85:
        return 'very'
    else:
        return 'eh'

def passed(score):

    if score.mean() > 60:
        return 'passed'
    else:
        return 'failed'

"""### Aggregation"""

df.groupby('faction').agg(score)

df.groupby('faction').agg(['count', 'mean', 'std', score])

df.groupby('faction').agg({'kind' : passed, 'brave' : score,
                                 'smart' : score, 'honest' : score,
                                 'selfless' : score})