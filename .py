import pandas as pd

df = pd.read_csv("Best Countries for Startups.csv")
df

turkey = df.loc[(df["country"]=="Turkey")]
turkey 

df.describe()

turkeytotal = df.sort_values("total score") 
turkeytotal.head(46)

turkeyquantity = df.sort_values("quantity score") 
asd.head(57)

turkeytotal = df.sort_values("quality score") 
turkeytotal.head(58)

turkeytotal = df.sort_values("quality score") 
turkeytotal.head(57)
