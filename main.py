from pyscript import display, document

# create a list
classmates = []

class Student:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

# add student
def add_student(event=None):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    person = Student(name, section, subject)

    # add student to list
    classmates.append(person)

    introduce()

# loop classmates
def show_classmates(e):
    document.getElementById('output').innerHTML = ""
    
    person1 = Student("Ainah", "Sapphire", "Social Studies")
    person2 = Student("Mergal", "Sapphire", "Math")
    person3 = Student("Margo", "Sapphire", "Social Studies")
    person4 = Student("Atasha", "Sapphire", "English")
    person5 = Student("Vito", "Sapphire", "Filipino")

    people = [person1, person2, person3, person4, person5]

    for student in people:
        display(f'Hi! I am {student.name}. I am from {student.section}. My favorite subject is {student.subject}', target="output")

# display the added student
def introduce():
    output_text = ""
    for student in classmates:
        output_text = f"Hi! I am {student.name}. I am from {student.section}. My favorite subject is {student.subject}"

    display(output_text, target="output")