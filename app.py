import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class GarageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LIFO Parking Garage System")
        self.root.geometry("500x600")
        
        self.garage = []

        self.title_label = tk.Label(root, text="LIFO Parking Garage", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        self.display_frame = tk.LabelFrame(root, text="Cars in Garage (LIFO - Top is Exit)")
        self.display_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.listbox = tk.Listbox(self.display_frame, font=("Courier", 10))
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)
        
        tk.Label(self.input_frame, text="Plate Number:").grid(row=0, column=0)
        self.plate_entry = tk.Entry(self.input_frame)
        self.plate_entry.grid(row=0, column=1, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = GarageApp(root)
    root.mainloop()