# # Apple Stock
# ### Introduction:
# We are going to use Apple's stock price.
# ### Step 1. Import the necessary libraries
import pandas as pd
from pandas.tseries.offsets import MonthEnd
import matplotlib.pyplot as plt
plt.style.use("dark_background")
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)
# #### Step 3. Assign it to a variable apple
apple = pd.read_csv("appl_1980_2014.csv")
# ### Step 4.  Check out the type of the columns
apple.dtypes
# ### Step 5. Transform the Date column as a datetime type
apple["Date"] = pd.to_datetime(apple["Date"])
apple.dtypes
# ### Step 6.  Set the date as the index
apple.set_index("Date", inplace=True)
apple.head()
# ### Step 7.  Is there any duplicate dates?
len(apple[apple.duplicated(keep=False)])
# ### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple.sort_index(inplace=True)
apple.head()
# ### Step 9. Get the last business day of each month
apple["EndMonth"] = apple.index + MonthEnd(1)
apple.groupby("EndMonth").last().head()
# ### Step 10.  What is the difference in days between the first day and the oldest
(apple.index[-1] - apple.index[0]).days
# ### Step 11.  How many months in the data we have?
((apple.index[-1] - apple.index[0])/30).days
# ### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
plt.figure(figsize=(13.5, 9))
_ = apple["Adj Close"].plot()
# ### What is the highest `Adj Close` to date?
apple["Adj Close"].idxmax()
