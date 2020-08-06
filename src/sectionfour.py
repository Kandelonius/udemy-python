my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}


def average_calculator(student):
    average = 0
    count = 0
    total = 0
    for n in student['grades']:
        total += n
        count += 1
    average = total / count
    return average
    # return sum(student['grades'])/len(student['grades'])


print(average_calculator(my_student))


class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Rolf Smith", [70, 88, 90, 99])
student_two = Student("Jose", [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)
print(student_one.__class__)
print(student_one.average())
print(student_one.grades)

def average(student):
    return sum(student.grades)/len(student.grades)

print(average(student_one))


### exercise start ###

# Define a Movie class that has two properties: name and director
class Movie():
    def __init__(self, movie_name, director_name):
        self.name = movie_name
        self.director = director_name

    # let's try to add a method `print_info()` here:
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")


# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')

print(my_movie.name)
my_movie.print_info()

### exercise end ###
