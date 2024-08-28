class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []

    def register_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Đã đăng ký môn học: {subject}")
        else:
            print(f"Môn học {subject} đã được đăng ký trước đó.")

    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")
        print(f"Lớp: {self.grade}")
        print("Các môn học đã đăng ký:", ", ".join(self.subjects) if self.subjects else "Chưa đăng ký môn học nào")

    def deregister_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"Đã hủy đăng ký môn học: {subject}")
        else:
            print(f"Môn học {subject} không tồn tại trong danh sách đăng ký.")

def main():
    student = Student("Pham Hoai Nam", 100, "1000A1")
    
    while True:
        command = input("Nhập lệnh (register/show/deregister/exit): ").strip().lower()
        
        if command == "register":
            subject = input("Nhập tên môn học để đăng ký: ").strip()
            student.register_subject(subject)
        
        elif command == "show":
            student.show_info()
        
        elif command == "deregister":
            subject = input("Nhập tên môn học để hủy đăng ký: ").strip()
            student.deregister_subject(subject)
        
        elif command == "exit":
            print("Thoát chương trình.")
            break
        
        else:
            print("Lệnh không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()