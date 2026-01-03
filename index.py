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