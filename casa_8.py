# implement a program that iterates the data inside of **big-mac-full-index.csv** on **casa_8.py** using the following methods from the tutorial:

import pandas as pd
df = pd.read_csv('big-mac-full-index.csv')
print("Given Dataframe :\n", df)

# 1. Method 4: Using iterrows() method
print("\nIterating over rows using iterrows() method :\n")

for index, row in df.iterrows():
    print(row["name"], row["local_price"])

# 2. Method 6: Using apply() method
print("\nIterating over rows using apply function :\n")

print(df.apply(lambda row: row["name"] + " " +
               str(row["local_price"]), axis=1))
