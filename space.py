# Space Trip Timer
# Calculates how long it takes to reach space objects, including stars, based on speed

def travel_time_calculator():
    # Distances to space objects from Earth in kilometers (average)
    distances = {
        # Planets
        "Mercury": 91000000,      # 91 million km
        "Venus": 41000000,        # 41 million km
        "Earth": 0,               # We're already here, but included for completeness
        "Mars": 78000000,         # 78 million km
        "Jupiter": 628000000,     # 628 million km
        "Saturn": 1275000000,     # 1.275 billion km
        "Uranus": 2721000000,     # 2.721 billion km
        "Neptune": 4351000000,    # 4.351 billion km
        
        # Notable Moons
        "Moon": 384400,           # 384,400 km (Earth's Moon)
        "Titan": 1276000000,      # 1.276 billion km (Saturn's largest moon)
        "Europa": 629000000,      # 629 million km (Jupiter's moon)
        "Ganymede": 629000000,    # 629 million km (Jupiter's largest moon)
        "Callisto": 629000000,    # 629 million km (Jupiter's moon)
        "Io": 629000000,          # 629 million km (Jupiter's moon)
        
        # Dwarf Planets
        "Pluto": 5906000000,      # 5.906 billion km
        "Ceres": 413000000,       # 413 million km (asteroid belt)
        "Eris": 10120000000,      # 10.12 billion km (scattered disc)
        "Haumea": 6480000000,     # 6.48 billion km (Kuiper Belt)
        "Makemake": 6850000000,   # 6.85 billion km (Kuiper Belt)
        
        # Other Solar System Objects
        "Sun": 149600000,         # 149.6 million km
        
        # Nearby Stars (converted from light-years to km, 1 ly ≈ 9.46 trillion km)
        "Proxima Centauri": 40100000000000,  # 4.24 light-years ≈ 40.1 trillion km
        "Alpha Centauri A": 41300000000000,  # 4.37 light-years ≈ 41.3 trillion km
        "Alpha Centauri B": 41300000000000,  # 4.37 light-years ≈ 41.3 trillion km
        "Barnards Star": 56500000000000     # 5.98 light-years ≈ 56.5 trillion km
    }
    
    print("Welcome to Space Trip Timer!")
    print("Destinations: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, "
          "Moon, Titan, Europa, Ganymede, Callisto, Io, "
          "Pluto, Ceres, Eris, Haumea, Makemake, Sun, "
          "Proxima Centauri, Alpha Centauri A, Alpha Centauri B, Barnards Star")
    
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
    time_years = time_days / 365
    
    # Display results
    print(f"\nTrip to {destination}:")
    print(f"Distance: {distance:,} km")
    print(f"Traveling at {speed:,} km/h:")
    print(f"- Time in hours: {time_hours:.2f}")
    print(f"- Time in days: {time_days:.2f}")
    print(f"- Time in years: {time_years:.2f}")

# Run the program
travel_time_calculator()
