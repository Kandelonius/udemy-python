age = 30

print(age)

age = 40
print('age is '+ str(age))

PI = 3.14159
RADIANS_TO_DEGREES = 180 / PI

_var = 80

float_division = 8/3
print(float_division)

integer_division = 8//3
print(integer_division) #truncates the result

integer_division = 13//5
print(integer_division) #truncates the result

remainder = 13%5
print(remainder)

x = 37
remainder = x % 2
print('remainder of 37%2 is ' + str(remainder))

#### challenge start ####

# Create two variables, var1 and var2, both with the same value.
# Create two variables, num1 and num2, which multiply together to give 16.

var1 = 37
var2 = 37
num1 = 8
num2 = 2

#### challenge end ####

string_with_single_quotes = "Could you do the egg bacon spam and sausage without the spam then"
string_with_character_cancel = "the vikings said \"Lovely spam! Wonderful spam!\""
string_with_double_quotes = "You can't have egg bacon spam and sausage without the spam"
multiline = """this
is
one
string
similar to /*
*/"""

explanation = "manual string formatting can get tedius like what was done in line "
line = 6
expcontinue = " so we can use print(f\"\") instead"
print(f"{explanation}{line}{expcontinue} this is an example")

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

#another example

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name=name) #this one refers to the variable name above
print(jose_greeting)

# error_greeting = f'How are you, {error}'
# print(error_greeting)

# I don't know
description = "{} is {} years old."
print(description.format("Bob", 30))

description = "{} is {age} years old."
print(description.format("Bob", age=30))

my_name = "Jose"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}.")
age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num*12} months... roughly.")

#### challenge start ####

# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).

name = input("Please enter your name: ")
print(f"Hello, {name}")

age = input("Please enter your age: ")
int_age = int(age)
print(f"{int_age*12}")

#### challenge end ####