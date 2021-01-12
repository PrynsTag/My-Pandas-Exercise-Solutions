# # Occupation
# ### Introduction:
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
# ### Step 3. Assign it to a variable called users.
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep="|", index_col="user_id")
users.head()

# ### Step 4. Discover what is the mean age per occupation
users.groupby("occupation")["age"].mean()
# ------ OR ------ # 
pd.pivot_table(users, index="occupation", values="age")  # default aggregator is mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least
def ratio(row):
    unique_occupation = users["occupation"].value_counts()
    return round((row / unique_occupation) * 100, 2)


users[users["gender"] == "M"].groupby("occupation").count().apply(ratio)["gender"]
# ------ OR ------ # 
pd.pivot_table(users[users["gender"] == "M"],
               index="occupation",
               values="gender",
               aggfunc="count").apply(ratio).sort_values(by="gender", ascending=False).rename(
    columns={"gender": "Male Ratio"})

# ### Step 6. For each occupation, calculate the minimum and maximum ages
users.groupby("occupation")["age"].agg(["min", "max"])
# ------ OR ------ # 
pd.pivot_table(users, index="occupation", values="age", aggfunc=["min", "max"])

# ### Step 7. For each combination of occupation and gender, calculate the mean age
users.groupby(['occupation', 'gender']).age.mean()
# ------ OR ------ # 
pd.pivot_table(users,
               index="occupation",
               columns="gender",
               values="age",
               aggfunc="mean").round(0)

# ### Step 8.  For each occupation present the percentage of women and men
gender_count = users.groupby(["occupation", "gender"]).agg({"gender": "count"})
occupation_count = users.groupby("occupation").count()
occup_gender = gender_count.div(occupation_count, level="occupation") * 100
occup_gender.loc[:, "gender"]
# ------ OR ------ # 
pd.pivot_table(users,
               index="occupation",
               values="age",
               columns="gender",
               aggfunc="count").apply(ratio)
