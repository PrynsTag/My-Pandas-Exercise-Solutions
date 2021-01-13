# # Regiment
# ### Introduction:
# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Create the DataFrame with the following values:
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
       'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
       'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
       'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
       'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# ### Step 3. Assign it to a variable called regiment.
# #### Don't forget to name each column
regiment = pd.DataFrame(raw_data)
regiment

# ### Step 4. What is the mean preTestScore from the regiment Nighthawks?  
regiment.groupby("regiment").mean().loc["Nighthawks", "preTestScore"]
# ------ OR ------ #
pd.pivot_table(regiment, index="regiment")

# ### Step 5. Present general statistics by company
regiment.groupby("company").describe().stack()
# ------ OR ------ #
pd.pivot_table(regiment, index="company", aggfunc="describe").stack()

# ### Step 6. What is the mean of each company's preTestScore?
regiment.groupby("company").mean()["preTestScore"]
# ------ OR ------ #
pd.pivot_table(regiment, index="company", values="preTestScore")

# ### Step 7. Present the mean preTestScores grouped by regiment and company
regiment.groupby(["regiment", "company"]).mean()["preTestScore"]
# ------ OR ------ #
pd.pivot_table(regiment, index=["regiment", "company"], values="preTestScore")["preTestScore"]

# ### Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
pd.pivot_table(regiment, index="regiment", columns="company", values="preTestScore")
# ------ OR ------ #
regiment.groupby(["regiment", "company"]).mean()["preTestScore"].unstack()

# ### Step 9. Group the entire dataframe by regiment and company
regiment.groupby(["regiment", "company"]).mean()
# ------ OR ------ #
pd.pivot_table(regiment, index=["regiment", "company"])

# ### Step 10. What is the number of observations in each regiment and company
regiment.groupby(["company", "regiment"]).size()
# ------ OR ------ #
pd.pivot_table(regiment, index=["company", "regiment"], aggfunc="size"

# ### Step 11. Iterate over a group and print the name and the whole data from the regiment
for name, group in regiment.groupby("regiment"):
   print(name)
   print(group)
