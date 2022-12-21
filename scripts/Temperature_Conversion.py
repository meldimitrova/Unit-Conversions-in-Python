# @author Melina Dimitrova

# Temperature Conversion
## Define a function

def temp_coversion(temp, current_unit, to_be_converted):
#Use "F" for Fahrenheit, "C" for Celsius and "K" for Kelvin
## Coversion from Celsius to Fahrenheit
    if to_be_converted == "F" and current_unit == "C":
        new_temp = round(9/5 * temp + 32, 3)
        print("The temperature from Celsius in Fahrenheit is "
              + str(new_temp) + "F")

## Coversion from Fahrenheit to Celcius
    elif to_be_converted == "C" and current_unit == "F":
        new_temp = round(5/9 * (temp - 32), 3)
        print("The temperature from Fahrenheit in Celsius is "
              + str(new_temp) + "C")

## Coversion from Celsius to Kelvin
    elif to_be_converted == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The temperature from Celsius in Kelvin is "
              + str(new_temp) + "K")

## Coversion from Kelvin to Celsius
    elif to_be_converted == "C" and current_unit == "K":
        new_temp = round(temp - 273.15, 3)
        print("The temperature from Kelvin in Celsius is "
              + str(new_temp) + "C")

## Coversion from Kelvin to Fahrenheit
    elif to_be_converted == "F" and current_unit == "K":
        new_temp = round(9/5 * (temp - 273.15) + 32, 3)
        print("The temperature from Kelvin in Fahrenheit is "
              + str(new_temp) + "F")

## Coversion from Fahrenheit to Kelvin
    else:
        new_temp = round(5/9 * (temp - 32) + 273.15, 3)
        print("The temperature from Fahrenheit in Kelvin is "
              + str(new_temp) + "K")


### With set values

temp_coversion(108,"C","F")
temp_coversion(235,"F","K")


### With user input

a = input("Input the temperature value you'd like to convert : ")
t = int(a) # conversion of string to int
b = input("Input the scale you're converting from (C, F or K) : ")
c = input("Input the scale you'd like to convert to (C, F or K) : ")

temp_coversion(t,b,c)
