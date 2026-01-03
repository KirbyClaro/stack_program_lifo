from datetime import datetime

def parking_garage():
    garage = []
    
    print("--- LIFO Parking Garage Simulation ---")
    print("System initialized. Garage is empty.")
    
    while True:
        print(f"\nCars in garage (Total: {len(garage)}):")
        for i, car in enumerate(reversed(garage)):
            print(f"  [Exit - {i}] Plate: {car['plate']} (Arrived: {car['arrival']})")
        
        print("\nOptions: [1] Arrival  [2] Departure  [3] Exit System")
        choice = input("Select an option: ")

        if choice == '1':
            plate = input("Enter car plate number: ").upper()
            arrival_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            car_data = {
                "plate": plate,
                "arrival": arrival_time
            }
            garage.append(car_data)
            print(f"Successfully parked: {plate} at {arrival_time}")
            
        elif choice == '2':
            if not garage:
                print("Error: The garage is empty!")
                continue
            
            # In a stack, we can only access the LAST item added
            top_car = garage[-1]
            print(f"\nCar at the exit: {top_car['plate']}")
            confirm_plate = input("Confirm plate number to depart: ").upper()

            if confirm_plate == top_car['plate']:
                departure_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Pop the car from the stack
                removed_car = garage.pop()
                print(f"\nDEPARTURE RECEIPT:")
                print(f"Plate: {removed_car['plate']}")
                print(f"Arrival: {removed_car['arrival']}")
                print(f"Departure: {departure_time}")
                print("Status: Car has safely left the garage.")
            else:
                print(f"Error: Car {confirm_plate} is blocked! {top_car['plate']} must leave first.")

        elif choice == '3':
            print("System shutting down...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    parking_garage()