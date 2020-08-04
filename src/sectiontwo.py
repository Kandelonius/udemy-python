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
is_learning = True
while is_learning:
    print("You're learning!")
    user_input = input("Are you still learning?")
    is_learning = user_input == "yes"

user_input2 = input("Do you wish to run the program? (yes/no): ")

while user_input2 == "yes":
    print("We're runnint!")
    user_input2 = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")
