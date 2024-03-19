import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog

def read_csv_and_plot_2d(csv_file):
    # Read the CSV data into a DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("File not found. Make sure the CSV file exists.")
        return
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        return
    except pd.errors.ParserError:
        print("Error parsing the CSV file. Please check the file format.")
        return

    # Update column names to match your CSV
    if 'X' in df and 'Y' in df:
        x = df['X']
        y = df['Y']

        # Create a 2D plot with lines
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, color='b', marker='o', linestyle='-')
        plt.title('2D Graph')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()
    else:
        print("CSV file must contain 'X' and 'Y' columns for plotting.")

def read_csv_and_plot_3d(csv_file):
    # Read the CSV data into a DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("File not found. Make sure the CSV file exists.")
        return
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        return
    except pd.errors.ParserError:
        print("Error parsing the CSV file. Please check the file format.")
        return

    # Update column names to match your CSV (X, Y, Z)
    if 'X' in df and 'Y' in df and 'Z' in df:
        x = df['X']
        y = df['Y']
        z = df['Z']

        # Create a 3D plot with lines
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, color='b', marker='o', linestyle='-')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_title('3D Graph')
        plt.show()
    else:
        print("CSV file must contain 'X', 'Y', and 'Z' columns for 3D plotting.")

def open_csv_file_2d():
    file_path = filedialog.askopenfilename(title="Select 2D CSV File")
    if file_path:
        read_csv_and_plot_2d(file_path)

def open_csv_file_3d():
    file_path = filedialog.askopenfilename(title="Select 3D CSV File")
    if file_path:
        read_csv_and_plot_3d(file_path)

root = tk.Tk()
root.title("CSV Plotter")

# Buttons for 2D and 3D file selection
button_2d = tk.Button(root, text="Select 2D CSV File", command=open_csv_file_2d)
button_3d = tk.Button(root, text="Select 3D CSV File", command=open_csv_file_3d)

button_2d.pack()
button_3d.pack()

root.mainloop()
