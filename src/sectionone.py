age = 30

print(age)

age = 40
print('age is ' + str(age))

PI = 3.14159
RADIANS_TO_DEGREES = 180 / PI

_var = 80

float_division = 8/3
print(float_division)

integer_division = 8//3
print(integer_division)  # truncates the result

integer_division = 13//5
print(integer_division)  # truncates the result

remainder = 13 % 5
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
string"""

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

# another example

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)

name = "Jose"
final_greeting = "How are you, {name}?"
# this one refers to the variable name above
jose_greeting = final_greeting.format(name=name)
print(jose_greeting)

# error_greeting = f'How are you, {error}'
# print(error_greeting)

# I don't know
description = "{} is {} years old."
print(description.format("Bob", 30))

description = "{} is {age} years old."
print(description.format("Bob", age=30))

# my_name = "Jose"
# your_name = input("Enter your name: ")

# print(f"Hello {your_name}. My name is {my_name}.")
# age = input("Enter your age: ")
# age_num = int(age)
# print(f"You have lived for {age_num*12} months... roughly.")

#### challenge start ####

# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).

# name = input("Please enter your name: ")
# print(f"Hello, {name}")

# age = input("Please enter your age: ")
# int_age = int(age)
# print(f"{int_age*12}")

#### challenge end ####

# my_number = 5
# user_number = int(input("Enter a number: "))

# matches = my_number == user_number

# print(f"You got it right? {matches}")

x = True and False
print(f"x = True and False: {x}")

x = 35 and 0
print(f"x = 35 and 0: {x}")

x = 0 and 35
print(f"x = 0 and 35: {x}")

x = 35 and 1
print(f"x = 35 and 1: {x}")

x = 1 and 35
print(f"x = 1 and 35: {x}")

x = True or False
print(f"x = True or False: {x}")

x = 35 or 0
print(f"x = 35 or 0: {x}")

x = 0 or 35
print(f"x = 0 or 35: {x}")

x = 35 or 1
print(f"x = 35 or 1: {x}")

x = 1 or 35
print(f"x = 1 or 35: {x}")

name = ""
surname = "Smith"

greeting = name or f"Mr. {surname}"
print(greeting)

# age = int(input("Enter your age: "))  #outputs True when given any number it seems
# side_job = True  # changing side_job to false actually shows when a different part
# print(age > 18 and age < 65 or side_job)  # is evaluated

# lists

friends = ["Rolf", "Bob", "Anne"]

print(friends[0])
print(friends[1])

print(len(friends))

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

friends[0][0]  # prints Rolf
friends[0][1]  # prints 24 for Rofls age

friends.append(["Jen, 32"])
print(friends)

friends.remove(["Rolf", 24])
print(friends)

short_tuple = ("Rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]
short_tuple = short_tuple + ("Jen",)
print(short_tuple)

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends)

art_friends.remove("Jen")

scifi_friends = {"Will", "Felicia", "Doug"}
fantasy_friends = {"Doug", "Tessa"}

scifi_but_not_fantasy = scifi_friends.difference(fantasy_friends)

print(
    f"the sci-fi friends who don't care for fantasy are {scifi_but_not_fantasy}")

scifi_and_fantasy_friends = scifi_friends.intersection(fantasy_friends)

print(
    f"the friends who like sci-fi and fantasy are {scifi_and_fantasy_friends}")

all_friends = scifi_friends.union(fantasy_friends)

print(f"all of the friends are {all_friends}")

#### challenge start ####

# nearby_people = {'Rolf', 'Jen', 'Anna'}
# user_friends = set()  # This is an empty set, like {}

# # # Ask the user for the name of a friend
# new_friend = input("enter the name of a close friend of yours: ")

# # # Add the name to the empty set
# user_friends.add(new_friend)

# # # Print out the intersection between both sets. This gives us a set with those
# # friends that are nearby.
# print(nearby_people.intersection(user_friends))

#### challenge end ####

# Dictionaries
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20

friend_ages["Rolf"] = 25

print(friend_ages)

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[1]["name"])

tuple_to_dict = [("Rolf", 24), ("Bob", 31)]
friend_ages = dict(tuple_to_dict)
print(friend_ages)

#### challenge start ####

lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        "name": "Scott",
        "numbers": {4, 98, 42, 27}
    },
    {
        "name": "Charlie",
        "numbers": {49, 21, 5, 82}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers
right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched 
with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their 
numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
player_one = players[0]["numbers"].intersection(lottery_numbers)
player_two = players[1]["numbers"].intersection(lottery_numbers)
player_one_name = players[0]["name"]
player_two_name = players[1]["name"]

print(f"Player {player_one_name} got {len(player_one)} numbers right")
print(f"Player {player_two_name} got {len(player_two)} numbers right")

#### challenge end ####

friends = ["Rolf", "Bob", "Anne"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")

comma_separated2 = " & ".join(friends)
print(f"My friends are {comma_separated2}.")