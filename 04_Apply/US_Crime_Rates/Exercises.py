# ### Introduction:
# This time you will create a data
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv).
# ### Step 3. Assign it to a variable called crime.
crime = pd.read_csv("US_Crime_Rates_1960_2014.csv")
crime.head()

# ### Step 4. What is the type of the columns?
crime.dtypes

# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# ### Step 5. Convert the type of the column Year to datetime64
crime["Year"] = pd.to_datetime(crime["Year"], format="%Y")
crime.info()

# ### Step 6. Set the Year column as the index of the dataframe
crime.set_index("Year", inplace=True)

# ### Step 7. Delete the Total column
crime.drop("Total", axis=1, inplace=True)

# ### Step 8. Group the year by decades and sum the values
# #### Pay attention to the Population column number, summing this column is a mistake
grouped = crime.groupby((crime.index.year//10)*10).sum().sort_values(by="Violent", ascending=False)

# ### Step 9. What is the most dangerous decade to live in the US?
grouped.idxmax()
