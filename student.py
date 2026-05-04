class Student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def get_letter_grade(self):
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        elif self.grade >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject,
            "grade": self.grade,
            "letter": self.get_letter_grade()
        }