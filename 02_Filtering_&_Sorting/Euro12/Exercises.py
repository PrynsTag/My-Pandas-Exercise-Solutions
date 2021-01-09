# # Ex2 - Filtering and Sorting Data
# ### Step 1. Import the necessary libraries
import pandas as pd
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). 
# ### Step 3. Assign it to a variable called euro12.
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
euro12 = pd.read_csv(url)
# ### Step 4. Select only the Goal column.
euro12["Goals"]
# ### Step 5. How many team participated in the Euro2012?
len(euro12["Team"].unique())
# ### Step 6. What is the number of columns in the dataset?
len(euro12.columns)
# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]
# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline.sort_values(by=["Red Cards", "Yellow Cards"], ascending=False)
# ### Step 9. Calculate the mean Yellow Cards given per Team
pd.pivot_table(euro12, values='Yellow Cards', index="Team", aggfunc="mean").mean().round()
euro12["Yellow Cards"].mean().round()
# ### Step 10. Filter teams that scored more than 6 goals
euro12[euro12["Goals"] > 6]
# ### Step 11. Select the teams that start with G
euro12[euro12["Team"].str.startswith("G")]
# ### Step 12. Select the first 7 columns
euro12.iloc[:, :7]
# ### Step 13. Select all columns except the last 3.
euro12.iloc[:, :-3]
# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia
teams = (euro12["Team"] == "England") | (euro12["Team"] == "Italy") | (euro12["Team"] == "Russia" )
euro12.loc[teams][["Team", "Shooting Accuracy"]]
