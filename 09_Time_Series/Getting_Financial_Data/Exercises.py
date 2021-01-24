# # Getting Financial Data - Pandas Datareader
# ### Introduction:
# This time you will get data from a website.
# ### Step 1. Import the necessary libraries
import pandas as pd
import datetime
import pandas_datareader.data as web
import requests_cache

# ### Step 2. Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is).
past = (datetime.datetime.strptime("01/01/2015", "%m/%d/%Y")).date()
present = datetime.date.today()
pd.date_range(past, present).tolist()[:5]

# ### Step 3. Get an API key for one of the APIs that are supported by Pandas Datareader, preferably for AlphaVantage.
# If you do not have an API key for any of the supported APIs, it is easiest to get one for [AlphaVantage]
# (https://www.alphavantage.co/support/#api-key). (Note that the API key is shown directly after the signup. You do *not* receive it via e-mail.)
# (For a full list of the APIs that are supported by Pandas Datareader, [see here](https://pydata.github.io/pandas-datareader/readers/index.html).
# As the APIs are provided by third parties, this list may change.)
# ### Step 4. Use Pandas Datarader to read the daily time series for the Apple stock (ticker symbol AAPL) between 01/01/2015 and today, assign it to df_apple and print it.
API_KEY = "#" 
df_apple = web.DataReader('AAPL', "av-daily", start=past, end=present, api_key=API_KEY)
df_apple.head()

# ### Step 5. Add a new column "stock" to the dataframe and add the ticker symbol
df_apple["stock"] = "AAPL"

# ### Step 6. Repeat the two previous steps for a few other stocks, always creating a new dataframe: Tesla, IBM and Microsoft. (Ticker symbols TSLA, IBM and MSFT.)
# Caching
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name="cache", backend="sqlite", expire_after=expire_after)
ticker_symbols = ["TSLA", "IBM", "MSFT"]
df_name = ["df_tesla", "df_ibm", "df_microsoft"]
for name, ticker in zip(df_name, ticker_symbols):
  vars()[name] = web.DataReader(ticker, "av-daily", start=past, end=present, api_key=API_KEY, session=session)
  vars()[name]["stock"] = ticker

# ### Step 7. Combine the four separate dataFrames into one combined dataFrame df that holds the information for all four stocks
df = [df_apple, df_tesla, df_ibm, df_microsoft]
combined = pd.concat(df)
combined.rename_axis("Date", inplace=True) # Rename index to "Date"
combined.index = pd.to_datetime(combined.index) # Convert index to datetime

# ### Step 8. Shift the stock column into the index (making it a multi-level index consisting of the ticker symbol and the date).
combined.set_index("stock", append=True, inplace=True)
combined

# ### Step 9. Create a dataFrame called vol, with the volume values.
vol = combined["volume"]
vol.head()

# ### Step 10. Aggregate the data of volume to weekly.
# Hint: Be careful to not sum data from the same week of 2015 and other years.
bi_weekly = vol.groupby([pd.Grouper(level='stock'), 
          pd.Grouper(level='Date', freq='W')]
        ).sum()
pd.DataFrame(bi_weekly)

# ### Step 11. Find all the volume traded in the year of 2015
reset_weekly = bi_weekly.reset_index(drop=False)
reset_weekly[(reset_weekly["Date"] >= "2015/01/01") & (reset_weekly["Date"] < "2016/01/01")]
