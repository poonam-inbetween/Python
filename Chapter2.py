# Exercise 2.2 Write a program that uses raw_input to prompt a user for their
# name and then welcomes them.

name = input("Enter your name \n")
print ("Hello ", name)

# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to
# compute gross pay

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25


Hours = input("Enter number of hours\n")
Rate = input("Enter the rate of payment\n")

Hours = float(Hours)
Rate = float(Rate)

Pay = Hours * Rate
print ("Pay = ", Pay)


# Exercise 2.4 Assume that we execute the following assignment statements:
			# width = 17
			# height = 12.0
# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
			# 1. width/2
			# 2. width/2.0
			# 3. height/3
			# 4. 1 + 2 * 5
# Use the Python interpreter to check your answers.


width = 17
height = 12.0

print("width/2 = ", width/2)
print ("width/2.0 = ", width/ 2.0)
print ("height/3 = ", height/3)
print ("1 + 2 * 5 = ", 1+2 * 5)


# Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit and print out the converted temperature.


Cel = input("Enter the temperature in Celsius which you wish to be converted \n")
fahren = float(Cel) * 1.8 + 32

print ("Temperature in Fahrenheit = ", fahren)