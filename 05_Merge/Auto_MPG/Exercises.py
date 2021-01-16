# # MPG Cars
# ### Introduction:
# 
# The following exercise utilizes data from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
# 
# ### Step 1. Import the necessary libraries
from numpy import random
import pandas as pd

# ### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv).  
#    ### Step 3. Assign each to a variable called cars1 and cars2
cars1 = pd.read_csv("./cars1.csv")
cars2 = pd.read_csv("./cars2.csv")
cars1.head()
cars2.head()

# ### Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1
cars1 = cars1.loc[:, :"car"]
cars1.head()

# ### Step 5. What is the number of observations in each dataset?
print("Cars1 Observations: {}".format(cars1.shape[0]))
print("Cars2 Observations: {}".format(cars2.shape[0]))

# ### Step 6. Join cars1 and cars2 into a single DataFrame called cars
cars = pd.concat([cars1, cars2], ignore_index=True)
cars.head()

# ### Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
owners = random.randint(15000, 73000, 398)

# ### Step 8. Add the column owners to cars
cars["owners"] = owners
cars.head()
