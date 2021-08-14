import pandas as pd
import numpy as np

data = np.array(["cagri", "yalniz"])
s = pd.Series(data) #default index 0,1,2,3,4....
print(s)

data2 = np.array(["cagri", "yalniz"])
s2= pd.Series(data2, index=[100,1001])
print(s2)


data3 = {"matematik": 100, "fizik": 50 }
s3 = pd.Series(data3)
print(s3)


s4 = pd.Series(data3, index=["fizik", "matematik"]) #yer degistirme icin kullanilabilir
print(s4)
print(s4[0])
print(s4["matematik"])
