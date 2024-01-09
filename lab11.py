from graph import animate
import pandas as pd

df = pd.read_csv('my_data.csv')
animate(df)

df = pd.read_csv('my_data2.csv')
animate(df)