# Alexander Mathias
# 02/06/25
# P1HW1
# Collecting user information

#get user info for integer numbers

base_value = int(input("Enter an integer as the base value: " ))
exponent = int(input("Enter an integer as the exponent: " )) 
print()
result = base_value ** exponent

print (base_value, "raised to the power of", exponent, "is", result, "!!")
print()
print("-" *5, "Addition and Substarction", "-" *4)
print()
starting_integer = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: " ))
subtract = int(input("Enter an integer to subtract: " ))
result = starting_integer + add - subtract
print()
print(starting_integer, "+", add, "-", subtract, "is equal to", result)
print()
