def main():
    temp:int = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (temp - 32) * 5.0/9.0
    print(f"{temp} degrees Fahrenheit is {degrees_celsius} degrees Celsius.")

if __name__ == '__main__':
    main()