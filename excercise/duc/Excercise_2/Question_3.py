class Student():
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []

    def register_subject(self, register_subject):
        self.subjects.append(register_subject)
        print(f'{register_subject} has been registered.')

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grade: {self.grade}')
        print(f"Registered Subjects: {', '.join(self.subjects) or 'No subjects registered'}")

    def deregister_subject(self, deregister_subject):
        if deregister_subject in self.subjects:
            self.subjects.remove(deregister_subject)
            print(f'{deregister_subject} has been deregistered')
        else:
            print(f'{deregister_subject} has not been registered before')


def main():
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        grade = input("Enter student's grade: ")

        student = Student(name, age, grade)

        while True:
            print("Choose your option: 'register', 'deregister', 'show', 'exit'")
            user_input = input("Your option: ")

            if user_input == 'register':
                register_subject = input("Enter the subject to register: ")
                student.register_subject(register_subject)

            elif user_input == 'deregister':
                deregister_subject = input("Enter the subject to deregister: ")
                student.deregister_subject(deregister_subject)

            elif user_input == 'show':
                student.show_info()

            elif user_input == 'exit':
                print("Exit the program.")
                break

            else:
                print("Invalid option.")
    
main()