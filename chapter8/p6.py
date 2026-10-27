#covert inchess to cm 
def inch_to_cm(inches):
    return inches * 2.54  
inches = float(input("Enter length in inches: "))

cm = inch_to_cm(inches)
print(f"Length in cm: {cm}")