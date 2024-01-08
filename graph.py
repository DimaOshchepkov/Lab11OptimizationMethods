import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    plt.cla()  # Очистить предыдущий график
    plt.plot(x_values[:frame], y_values[:frame], marker='o', linestyle='-', color='blue')
    plt.title('Перемещение точек по координатам')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid(True)

df = pd.read_csv('my_data.csv')
# Данные для анимации
x_values = df['0']
y_values = df['1']

fig = plt.figure(figsize=(8, 6))
ani = FuncAnimation(fig, update, frames=len(df), interval=200, repeat=False)

plt.show()

df = pd.read_csv('my_data2.csv')
fig = plt.figure(figsize=(8, 6))
ani = FuncAnimation(fig, update, frames=len(df), interval=200, repeat=False)

plt.show()