"""
friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print("I only have one friend and you are not it.")

print("this runs anyway")

name = input("Enter your name: ")

print(bool(name))

if name:
    print("We know your name.")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello friend!")
elif user_name in family:
    print("Hello family!")
else:
    print("I don't know you.")
"""
# is_learning = True
# while is_learning:
#     print("You're learning!")
#     user_input = input("Are you still learning?")
#     is_learning = user_input == "yes"
#
# user_input2 = input("Do you wish to run the program? (yes/no): ")
#
# while user_input2 == "yes":
#     print("We're runnint!")
#     user_input2 = input("Do you wish to run the program? (yes/no): ")
#
# print("We stopped running.")

#### challenge start ####

# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.


# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = input("Would you like to print or quit?")

# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
# while(user_input != 'q'):
#     if(user_input == 'p'):
#         print("Hello")

#    If they did, print "Hello"
# Still inside the loop, ask the user again
#     user_input = input("Would you like to print or quit?")

#### challenge end ####

friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print("hello " + str(index))

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")