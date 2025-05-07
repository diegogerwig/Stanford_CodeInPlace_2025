"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Get user input for Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Calculate Mars weight (37.8% of Earth weight)
    mars_weight = earth_weight * 0.378
    
    # Round to 2 decimal places
    mars_weight = round(mars_weight, 2)
    
    # Display the result
    print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == "__main__":
    main()