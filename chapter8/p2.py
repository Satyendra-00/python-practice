def temp(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius is:", temp(fahrenheit))