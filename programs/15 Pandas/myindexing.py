# we can able to change the indexing as we want
import pandas as pd
a=[4,5,6]
myvar=pd.Series(a,index=["X","Y","Z"])
print(myvar)