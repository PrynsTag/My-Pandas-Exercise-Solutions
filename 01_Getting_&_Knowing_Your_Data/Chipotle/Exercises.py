import numpy as np
import pandas as pd
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep="\t")
chipo.head(10)
chipo.shape[0]
len(chipo.iloc[:])
chipo.shape[1]
print(chipo.columns)
chipo.index
chipo.groupby("item_name").sum().sort_values(ascending=False, by="quantity").iloc[0].name
chipo.groupby("item_name").sum().sort_values(ascending=False, by="quantity")["quantity"][0]
chipo.groupby("choice_description").sum().sort_values(ascending=False, by="quantity").iloc[0].name
chipo["quantity"].sum()
chipo["item_price"].dtype
chipo["item_price"] = chipo["item_price"].apply(lambda col: col.replace("$", "")).astype("float")
chipo["item_price"].dtype
revenue = chipo["item_price"] * chipo["quantity"]
chipo["revenue"] = revenue
chipo["revenue"].sum()
chipo.groupby("order_id").sum().shape[0]
chipo.groupby("order_id").aggregate(np.sum)["revenue"].mean()
chipo.pivot_table(index="order_id", values="revenue", aggfunc=np.sum).mean().iloc[0]
chipo["item_name"].unique().shape[0]
