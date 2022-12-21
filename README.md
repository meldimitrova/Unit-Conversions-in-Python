# Unit Conversions in Python

This project demonstrates a variety of conversion techniques in Python, e.g. temperature conversion, length and mass units, calendar functions and timezones. The goal was to demonstrate the usage of Python as a programming languages and also use external libraries.

### Temperature conversion

This script performs temperature conversion between *Celsius, Fahrenheit* and *Kelvin* scales. The conversion is possible between all 3 scales as the code allows interaction between each set of pairs. The conversion is done with set values but also allows user input for values and desired scales.

### Unit conversion

The unit conversion is performed using an external library [Axiompy](https://github.com/ArztKlein/Axiompy) to convert and perform math operations on values of particular units. The package supports SI Base units and imperial units for length, time and mass. This script demonstrates how this conversion works with functions for the respective conversion operations.
A prerequisite is to install the Axiompy package via *pip install axiompy*.

### TimeZone

This script shows implements the **pytz** and datetime packages work to demonstrate how the timezone works and how to convert between the different time zones.

### Calendar

The calendar has two functions. The first one focuses on returning a weekday given a specific date which can be a set one or by taking user input of a date and breaking down the string into separate int variables. The second function is focused on the calendar feature that displays a specific month in the calendar whether by set variable or populated by user input.
