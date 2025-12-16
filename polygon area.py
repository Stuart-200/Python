import math

def calculate_triangle_area():
    """Calculates the area of a triangle given its base and height."""
    print("\n--- Triangle Area Calculation ---")
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if base <= 0 or height <= 0:
        print("Error: Base and height must be positive numbers.")
        return

    # Calculation and print statement are now inside the function
    areaT = 0.5 * base * height
    print(f"\nThe area of the triangle is: {areaT:.2f} square units.")
    # 



def calculate_square_area():
    """Calculates the area of a square given its side length."""
    print("\n--- Square Area Calculation ---")
    try:
        side = float(input("Enter the side length of the square: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if side <= 0:
        print("Error: Side length must be a positive number.")
        return

    # Calculation and print statement are now inside the function
    areaS = side * side
    print(f"\nThe area of the square is: {areaS:.2f} square units.")
    # 

def calculate_rectangle_area():
    """Calculates the area of a rectangle given its length and width."""
    print("\n--- Rectangle Area Calculation ---")
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if length <= 0 or width <= 0:
        print("Error: Length and width must be positive numbers.")
        return

    # Calculation and print statement are now inside the function
    areaR = length * width
    print(f"\nThe area of the rectangle is: {areaR:.2f} square units.")
    # 


def main():
    """Runs the interactive menu for the calculator."""
    while True:
        print("\n==============================")
        print("   Geometric Area Calculator")
        print("==============================")
        print("1: Calculate Triangle Area")
        print("2: Calculate Square Area")
        print("3: Calculate Rectangle Area")
        print("4: Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_triangle_area()
        elif choice == '2':
            calculate_square_area()
        elif choice == '3':
            calculate_rectangle_area()
        elif choice == '4':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()