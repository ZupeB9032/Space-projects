# Space Travel Time Calculator
# Calculates how long it takes to reach a planet based on speed

def travel_time_calculator():
    # Distances to planets from Earth in kilometers (average)
    distances = {
        "Mars": 78000000,    # 78 million km
        "Venus": 41000000,   # 41 million km
        "Moon": 384400       # 384,400 km
    }
    
    print("Welcome to Space Travel Calculator!")
    print("Available destinations: Moon, Venus, Mars")
    
    # Get user input for destination
    destination = input("Where do you want to go? ").capitalize()
    
    # Check if destination is valid
    if destination not in distances:
        print("Sorry, that destination isn't available!")
        return
    
    # Get travel speed from user
    speed = float(input("How fast will you travel (km/h)? "))
    
    # Ensure speed is positive
    if speed <= 0:
        print("Speed must be greater than 0!")
        return
    
    # Calculate travel time
    distance = distances[destination]
    time_hours = distance / speed
    time_days = time_hours / 24
    
    # Display results
    print(f"\nTrip to {destination}:")
    print(f"Distance: {distance:,} km")
    print(f"Traveling at {speed:,} km/h:")
    print(f"- Time in hours: {time_hours:.2f}")
    print(f"- Time in days: {time_days:.2f}")
travel_time_calculator()    