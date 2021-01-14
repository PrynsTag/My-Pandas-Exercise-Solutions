# # Student Alcohol Consumption
# ### Introduction:
# This time you will download a dataset from the UCI.
# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).
# ### Step 3. Assign it to a variable called df.
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv"
df = pd.read_csv(url)

# ### Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
df = df.loc[:, "school":"guardian"]

# ### Step 5. Create a lambda function that will capitalize strings.
capitalize = lambda element: element.str.capitalize()

# ### Step 6. Capitalize both Mjob and Fjob
df[["Mjob", "Fjob"]].apply(capitalize)

# ### Step 7. Print the last elements of the data set.
df.tail(1)

# ### Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
df[["Mjob", "Fjob"]] = df[["Mjob", "Fjob"]].apply(capitalize)
df.tail(1)

# ### Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(element):
    if element > 17:
        return True
    else:
        return False


df["legal_drinker"] = df["age"].apply(majority)

# ### Step 10. Multiply every number of the dataset by 10. 
# ##### I know this makes no sense, don't forget it is just an exercise
numeric_cols = [col for col in df.columns if df[col].dtypes == "int64"]
df[numeric_cols] = df[numeric_cols].apply(lambda element: element * 10)
