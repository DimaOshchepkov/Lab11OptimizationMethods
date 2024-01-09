import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(df: pd.DataFrame) -> None:
    def update(frame):
        plt.cla()  # Очистить предыдущий график
        plt.plot(x_values[:frame], y_values[:frame], marker='o', linestyle='-', color='blue')
        plt.title('Перемещение точек по координатам')
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.grid(True) 
        
    # Данные для анимации
    x_values = df['0']
    y_values = df['1']

    fig = plt.figure(figsize=(8, 6))
    ani = FuncAnimation(fig, update, frames=len(df), interval=200, repeat=False)

    plt.show()
