class Student:
    def __init__(self, name, grade, address):
        self.name = name
        self.grade = grade
        self.adress = address
        self.courses = {}
    def add_course(self, course):
        self.courses[course]=100 
        course.add_student(self)
    def dropout(self, course):
        del self.courses[course]
    def grading(self, points, course):
        self.courses[course]+=points/course.points
        print(self.courses[course])
class Courses:
    def __init__(self, name, weight, points):
        self.name = name
        self.weight = weight
        self.points = points
        self.students = []
    def add_student(self, name):
        self.students.append(name)
if __name__=="__main__":
    all_courses = []
    math = Courses("math", 4, 200)
    english = Courses("English", 4, 200)
    language = Courses("language", 4, 200)
    baking = Courses("baking", 3, 180)
    astudent = Student("aefjjjfd", 13, "here")
    astudent.add_course(math)
    astudent.grading(190, math)
    all_courses.append(math)
    all_courses
    