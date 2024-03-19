import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import can

# Global variables to store imported BLF and output ASC file paths
input_blf_file = ""
output_asc_file = ""

def convert_blf_to_asc(input_blf_file, output_asc_file):
    try:
        with can.BLFReader(input_blf_file) as log:
            with open(output_asc_file, 'w') as output_file:
                for msg in log:
                    output_file.write(msg.__str__() + '\n')
        print(f"Conversion completed. Data written to {output_asc_file}")
    except Exception as e:
        print(f"Error: {e}")

def import_file():
    global input_blf_file
    input_blf_file = filedialog.askopenfilename()
    if input_blf_file:
        # Clear the output file path when a new BLF file is imported
        selected_file_label.config(text="Selected File: " + input_blf_file)
        output_asc_file_label.config(text="Output File: ")
        
def convert():
    global input_blf_file, output_asc_file
    if input_blf_file:
        output_asc_file = filedialog.asksaveasfilename(defaultextension=".asc", filetypes=[("ASC Files", "*.asc")])
        if output_asc_file:
            convert_blf_to_asc(input_blf_file, output_asc_file)
            output_asc_file_label.config(text="Output File: " + output_asc_file)

root = tk.Tk()
root.geometry("440x400")
root.title("TATA Technologies - DoIP SW Deployer")
root.configure(bg='#FFFFFF')  # White background

# Stylish font
stylish_font = ("Arial", 10)

# Logo resizing
logo = Image.open("logo.png")
logo = logo.resize((150, 95))
logo = ImageTk.PhotoImage(logo)

# Selected file label
selected_file_label = tk.Label(root, text="Selected File: ", bg='#FFFFFF', font=stylish_font)
output_asc_file_label = tk.Label(root, text="Output File: ", bg='#FFFFFF', font=stylish_font)

# Buttons
import_file_button = tk.Button(root, text="Import BLF", command=import_file, bg='#F0F0F0', relief=tk.GROOVE, width=20, height=2, font=stylish_font)
convert_button = tk.Button(root, text="Convert to ASC", command=convert, bg='#F0F0F0', relief=tk.GROOVE, width=20, height=2, font=stylish_font)

# Logo Label
logo_label = tk.Label(root, image=logo, bg='#FFFFFF', relief=tk.SOLID, bd=1)

# Widget Placement using grid
logo_label.grid(row=0, column=0, columnspan=2, pady=15, padx=15)
selected_file_label.grid(row=1, column=0, columnspan=2, pady=10, padx=15)
output_asc_file_label.grid(row=2, column=0, columnspan=2, pady=10, padx=15)
import_file_button.grid(row=3, column=0, pady=10, padx=15)
convert_button.grid(row=3, column=1, pady=10, padx=15)

root.mainloop()
