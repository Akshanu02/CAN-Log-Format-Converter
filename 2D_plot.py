import pandas as pd
import matplotlib.pyplot as plt

def read_csv_and_plot(csv_file):
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

    # Assuming the CSV has columns 'x' and 'y', you can modify this based on your CSV structure
    if 'x' in df and 'y' in df:
        x = df['x']
        y = df['y']

        # Create a 2D plot
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, marker='o', s=50, color='b')
        plt.title('2D Graph')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()
    else:
        print("CSV file must contain 'x' and 'y' columns for plotting.")

if __name__ == "__main__":
    csv_file = input("Enter the CSV file path: ")
    read_csv_and_plot(csv_file)
