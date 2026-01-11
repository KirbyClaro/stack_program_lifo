import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ParkingGarageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LIFO Parking Management System")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f0f0")

        # Data structure: List acting as a Stack (LIFO)
        self.garage = []

        self.setup_ui()

    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill="x")
        
        tk.Label(
            header_frame, text="STACK PARAGE GARAGE", 
            fg="white", bg="#2c3e50", font=("Helvetica", 16, "bold")
        ).pack(pady=15)

        # Main Container
        main_content = tk.Frame(self.root, bg="#f0f0f0")
        main_content.pack(padx=20, pady=20, fill="both", expand=True)

        # Input Section
        input_label = tk.Label(main_content, text="Enter Plate Number:", bg="#f0f0f0", font=("Arial", 10))
        input_label.pack(anchor="w")
        
        self.plate_entry = ttk.Entry(main_content, font=("Arial", 12))
        self.plate_entry.pack(fill="x", pady=5)
        self.plate_entry.bind("<Return>", lambda e: self.park_car()) # Enter key support

        # Buttons
        btn_frame = tk.Frame(main_content, bg="#f0f0f0")
        btn_frame.pack(fill="x", pady=10)

        self.park_btn = ttk.Button(btn_frame, text="Park (Push)", command=self.park_car)
        self.park_btn.pack(side="left", expand=True, fill="x", padx=2)

        self.depart_btn = ttk.Button(btn_frame, text="Depart (Pop)", command=self.depart_car)
        self.depart_btn.pack(side="left", expand=True, fill="x", padx=2)

        # Display Section
        tk.Label(main_content, text="Current Garage Status (Exit at Top):", bg="#f0f0f0", font=("Arial", 10, "italic")).pack(anchor="w", pady=(10, 0))
        
        self.listbox = tk.Listbox(
            main_content, font=("Courier New", 11), 
            bg="white", height=12, selectmode=tk.SINGLE
        )
        self.listbox.pack(fill="both", expand=True, pady=5)

        # Footer Status
        self.status_var = tk.StringVar(value="Garage is empty.")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor="w")
        status_bar.pack(side="bottom", fill="x")

    def update_display(self):
        """Refreshes the Listbox to show the stack status."""
        self.listbox.delete(0, tk.END)
        # We reverse the list for display so the "Top" of the stack is visually at the top
        for i, car in enumerate(reversed(self.garage)):
            prefix = "[EXIT] -> " if i == 0 else f" [{len(self.garage)-i}] "
            self.listbox.insert(tk.END, f"{prefix} {car['plate']} | In: {car['arrival']}")
        
        self.status_var.set(f"Total Cars: {len(self.garage)}")

    def park_car(self):
        plate = self.plate_entry.get().upper().strip()
        if not plate:
            messagebox.showwarning("Input Required", "Please enter a car plate number.")
            return
        
        arrival_time = datetime.now().strftime("%H:%M:%S")
        car_data = {"plate": plate, "arrival": arrival_time}
        
        # LIFO 'Push'
        self.garage.append(car_data)
        
        self.update_display()
        self.plate_entry.delete(0, tk.END)

    def depart_car(self):
        if not self.garage:
            messagebox.showerror("Empty", "The garage is already empty!")
            return

        confirm_plate = self.plate_entry.get().upper().strip()
        if not confirm_plate:
            messagebox.showinfo("Instruction", "Please type the plate of the car at the exit to confirm.")
            return

        # LIFO 'Peek'
        top_car = self.garage[-1]

        if confirm_plate == top_car['plate']:
            # LIFO 'Pop'
            removed = self.garage.pop()
            self.update_display()
            self.plate_entry.delete(0, tk.END)
            
            messagebox.showinfo("Departure Success", 
                f"RECEPT\n{'-'*20}\nPlate: {removed['plate']}\nArrived: {removed['arrival']}\nDeparted: {datetime.now().strftime('%H:%M:%S')}")
        else:
            messagebox.showerror("Blocked", 
                f"Access Denied!\n\nCar '{confirm_plate}' is blocked by car '{top_car['plate']}'.\nLIFO rules apply: The last car in must be the first out.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingGarageApp(root)
    root.mainloop()