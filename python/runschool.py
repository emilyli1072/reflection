from school import Courses
from school import Student
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