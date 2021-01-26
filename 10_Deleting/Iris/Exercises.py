# # Iris
# ### Introduction:
# This exercise may seem a little bit strange, but keep doing it.
# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). 
# ### Step 3. Assign it to a variable called iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = pd.read_csv(url)
iris.head()

# ### Step 4. Create columns for the dataset
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class
iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
iris.head()

# ### Step 5.  Is there any missing value in the dataframe?
iris.isnull().sum()

# ### Step 6.  Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN
iris.loc[10:29, "petal_length"] = None

# ### Step 7. Good, now lets substitute the NaN values to 1.0
iris.fillna(1.0, inplace=True)
iris[10:29]

# ### Step 8. Now let's delete the column class
iris.drop("class", axis=1, inplace=True)
iris.head()

# ### Step 9.  Set the first 3 rows as NaN
iris.iloc[0:3] = None
iris.head()

# ### Step 10.  Delete the rows that have NaN
iris.dropna(axis=0, inplace=True)
iris.head()

# ### Step 11. Reset the index so it begins with 0 again
iris.reset_index(inplace=True)
iris.head()