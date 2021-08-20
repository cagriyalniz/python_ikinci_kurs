import pandas as pd
import matplotlib.pyplot
from sklearn.linear_model import LinearRegression

veri = pd.read_csv("hw_25000.csv")
print(veri.columns)

boy = veri.Height.values.reshape(-1,1)
kilo = veri.Weight.values.reshape(-1,1)
regression = LinearRegression()

regression.fit(boy, kilo)
print(regression.predict(71))
