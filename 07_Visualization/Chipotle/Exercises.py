# # Visualizing Chipotle's Data
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# set this so the graphs open internally
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("dark_background")

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
# ### Step 3. Assign it to a variable called chipo.
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep="\t")

# ### Step 4. See the first 10 entries
chipo.head(10)

# ### Step 5. Create a histogram of the top 5 items bought
top_5 = pd.pivot_table(chipo, index="item_name", values="quantity", aggfunc="sum").sort_values(by="quantity", ascending=True).tail(5)
_ = top_5.plot(kind="bar")

# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis
chipo["item_price"] = chipo["item_price"].str.replace("$", "").astype("float64")
grouped = chipo.groupby("order_id").sum()
_ = grouped.plot(kind="scatter", x="item_price", y="quantity")

# ### Step 7. BONUS: Create a question and a graph to answer your own question.
# #### Top 5 Largest Denomination paid
top_5 = grouped.sort_values("item_price", ascending=False).head(5)
_ = top_5["item_price"].plot(kind="bar", xlabel="order id", ylabel="Price")
