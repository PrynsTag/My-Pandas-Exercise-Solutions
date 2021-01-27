# # Wine
# ### Introduction:
# This exercise is a adaptation from the UCI Wine dataset.
# The only pupose is to practice deleting data with pandas.
# ### Step 1. Import the necessary libraries
import pandas as pd
import random

# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data). 
# ### Step 3. Assign it to a variable called wine
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(url)
wine.info()

# ### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine.drop(wine.iloc[:, [0, 3, 6, 8, 10, 12, 13]], axis=1, inplace=True)
wine.info()

# ### Step 5. Assign the columns as below:
# The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 
wine.columns = ["alcohol", "malic_acid", "alcalinity_of_ash", "magnesium", "flavanoids", "proanthocyanins", "hue"]
wine.head()

# ### Step 6. Set the values of the first 3 rows from alcohol as NaN
wine.loc[:2, "alcohol"] = None
wine.head()

# ### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
wine.loc[2:3, "magnesium"] = None
wine.head()

# ### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine["alcohol"].fillna(10, inplace=True)
wine["magnesium"].fillna(100, inplace=True)
# ### Step 9. Count the number of missing values
wine.isnull().sum()

# ### Step 10.  Create an array of 10 random numbers up until 10
rand_num = random.sample(range(0, 10), 10)
rand_num

# ### Step 11.  Use random numbers you generated as an index and assign NaN value to each of cell.
wine.iloc[rand_num] = None
wine.iloc[rand_num]

# ### Step 12.  How many missing values do we have?
wine.isnull().sum()

# ### Step 13. Delete the rows that contain missing values
wine.dropna(inplace=True)
wine.isnull().sum()

# ### Step 14. Print only the non-null values in alcohol
wine[wine["alcohol"] != None]["alcohol"]

# ### Step 15.  Reset the index, so it starts with 0 again
wine.reset_index(inplace=True)
wine.head()
