class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Student:
    def __init__(self, name, roll_number, subject_count):
        self.name = name
        self.roll_number = roll_number
        self.subjects = [None] * subject_count  # Fixed-size array
        self.subject_count = subject_count

    def set_subject(self, index, subject):
        if 0 <= index < self.subject_count:
            self.subjects[index] = subject


class ReportCard:
    def __init__(self, student):
        self.student = student
        self.total = 0
        self.average = 0.0
        self.grade = ""

    def calculate(self):
        total_marks = 0
        for i in range(self.student.subject_count):
            subject = self.student.subjects[i]
            if subject is not None:
                total_marks += subject.marks
        self.total = total_marks
        self.average = self.total / self.student.subject_count
        self.grade = self.get_grade()

    def get_grade(self):
        avg = self.average
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("~~~~ Report Card ~~~")
        print("Name:", self.student.name)
        print("Roll Number:", self.student.roll_number)
        print("Subjects and Marks:")
        for i in range(self.student.subject_count):
            sub = self.student.subjects[i]
            if sub:
                print(f"  {sub.name}: {sub.marks}")
        print("Total Marks:", self.total)
        print("Average:", self.average)
        print("Grade:", self.grade)
student = Student("Chetana", "101", 3)

student.set_subject(0, Subject("Math", 95))
student.set_subject(1, Subject("Science", 85))
student.set_subject(2, Subject("English", 90))

report = ReportCard(student)
report.calculate()
report.display_report()
