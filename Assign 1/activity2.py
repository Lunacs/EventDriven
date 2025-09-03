class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)

    def grade_category(self):
        # lambda to get symbol based on grade
        get_grade = lambda score: (
            'A' if 90 <= score <= 100 else
            'B' if 80 <= score < 90 else
            'C' if 70 <= score < 80 else
            'D' if 60 <= score < 70 else
            'F' if 0 <= score < 60 else
            'Invalid Grade'
        )
        return get_grade(self.average_grade())


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, index):
        print(f"\n👩‍🎓 Student {index+1}")
        name = input("Enter name: ").strip()

        while True:
            try:
                grades_limit = int(input("How many grades: "))
                if grades_limit > 0:
                    break
                print("Invalid input! Must be positive.")
            except ValueError:
                print("The amount should be an integer!")

        grades = []
        for i in range(grades_limit):
            while True:
                try:
                    grade = float(input(f"Enter grade {i + 1}: "))
                    if 0 <= grade <= 100:
                        grades.append(grade)
                        break
                    print("Invalid grade! Must be 0–100.")
                except ValueError:
                    print("The grade should be a number!")

        student = Student(name, grades)
        self.students.append(student)

        print(f"\n{name}'s average grade: {student.average_grade()}")
        print(f"{name}'s grade category: {student.grade_category()}")

    def show_all_students(self):
        print("\n📋 Student Records:")
        for student in self.students:
            print(f"{student.name} → Avg: {student.average_grade()} | Category: {student.grade_category()}")


if __name__ == '__main__':
    manager = GradeManager()

    # Ask how many students total
    while True:
        try:
            total_students = int(input("How many students to enter? "))
            if total_students > 0:
                break
            print("Invalid input! Must be positive.")
        except ValueError:
            print("The amount should be an integer!")

    # Fixed loop for students
    for i in range(total_students):
        manager.add_student(i)

    # Show all records
    manager.show_all_students()
    print("Bye bye! ＼（〇_ｏ）／")
