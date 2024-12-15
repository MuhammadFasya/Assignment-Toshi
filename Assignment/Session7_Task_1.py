'''
Totoro Transport System
'''
class Fahrzeug:
    def __init__(self, vehicle_type, distance):
        self.vehicle_type = vehicle_type
        self.distance = distance

    def get_distance(self):
        return self.distance

# Function to calculate the total distance
def calculate_total_distance(vehicles):
    total_distance = 0
    for vehicle in vehicles:
        total_distance += vehicle.get_distance()
    return total_distance

def main():
    # Input handling
    n = int(input("Enter the number of vehicles: "))
    vehicles = []

    for _ in range(n):
        line = input().split()
        vehicle_type = line[0]
        distance = int(line[1])
        vehicles.append(Fahrzeug(vehicle_type, distance))

    total_distance = calculate_total_distance(vehicles)
    print(f"Total distance: {total_distance}")

if __name__ == "__main__":
    main()
