import math

# Function to calculate and display trigonometric values
def trig_values(angle_degrees):
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sine, cosine, tangent
    sine = math.sin(angle_radians)
    cosine = math.cos(angle_radians)
    try:
        tangent = math.tan(angle_radians)
    except:
        tangent = "Undefined"  # For angles like 90°, 270°, etc.

    # Display the results
    print(f"\nTrigonometric values for {angle_degrees}°:")
    print(f"Sine: {sine}")
    print(f"Cosine: {cosine}")
    print(f"Tangent: {tangent}")

# Main program
angle = float(input("Enter an angle in degrees: "))
trig_values(angle)
