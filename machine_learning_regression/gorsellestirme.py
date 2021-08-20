import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("hw_25000.csv")

print(veri.columns)
plt.scatter(veri.Height, veri.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.show()