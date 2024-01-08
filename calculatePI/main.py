import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def estimate_pi(num_samples):
    inside_circle = 0
    points_inside_x = []
    points_inside_y = []

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1
            points_inside_x.append(x)
            points_inside_y.append(y)

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate, points_inside_x, points_inside_y

def plot_points_and_circle(ax, points_x, points_y):
    ax.scatter(points_x, points_y, color='blue', label='Points inside quarter circle')

    circle = Ellipse((0.5, 0.5), 1, 1, edgecolor='red', facecolor='none', linewidth=2, label='Inscribed quarter circle')
    ax.add_patch(circle)

def calculate_pi():
    num_samples = int(samples_entry.get())
    if num_samples <= 0:
        result_label.config(text="Number of samples should be greater than 0.")
        return

    pi_value, points_x, points_y = estimate_pi(num_samples)

    fig, ax = plt.subplots()
    plot_points_and_circle(ax, points_x, points_y)

    ax.set_title(f"Estimation of π: {pi_value}")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='datalim')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, column=0, columnspan=2)

    result_label.config(text=f"Estimated value of π using {num_samples} samples: {pi_value}")

# GUI setup
window = tk.Tk()
window.title("Monte Carlo π Estimation")

# Widgets
samples_label = tk.Label(window, text="Enter the number of samples:")
samples_label.grid(row=0, column=0, pady=5)

samples_entry = ttk.Entry(window)
samples_entry.grid(row=0, column=1, pady=5)

calculate_button = ttk.Button(window, text="Calculate π", command=calculate_pi)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
