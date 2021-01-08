# ### Step 1. Import the necessary libraries
import pandas as pd

# ### Step 2. Import the dataset from this [address](
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). ### Step 3. Assign it to a variable
# called chipo.
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep="\t")

# ### Step 4. How many products cost more than $10.00?
# #### Personal Step 4.1 Convert the item_price Column to float64
chipo["item_price"] = chipo["item_price"].str.replace("$", "").astype("float64")
chipo[chipo["item_price"] > 10.00]["item_price"].count()

# ### Step 5. What is the price of each item?
# ###### print a data frame with only two columns item_name and item_price
chipo[["item_name", "item_price"]]

# ### Step 6. Sort by the name of the item
chipo[["item_name", "item_price"]].sort_values(by="item_name")

# ### Step 7. What was the quantity of the most expensive item ordered?
chipo.sort_values(by="item_price", ascending=False)["quantity"].iloc[0]

# ### Step 8. How many times was a Veggie Salad Bowl ordered?
chipo[chipo["item_name"] == "Veggie Salad Bowl"]["quantity"].count()

# ### Step 9. How many times did someone order more than one Canned Soda?
chipo[(chipo["item_name"] == "Canned Soda") & (chipo["quantity"] > 1)].count().values[0]
