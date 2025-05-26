#!/usr/bin/env python3
"""
NASA Astronaut Height Checker
Checks if the user's height meets NASA astronaut requirements.
"""

def main():
    # Solicitar la altura al usuario
    height = float(input("Enter your height in meters: "))
    
    # Verificar los requisitos de altura para astronautas de la NASA
    if height > 1.6 and height < 1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    else:  # height >= 1.9
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()