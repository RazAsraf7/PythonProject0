initlist = []
class Student:
    def __init__(self, name, lastname, id, courselist, gradelist):
        initdict = {}
        self.name = name
        self.lastname = lastname
        self.id = id
        self.courselist = courselist
        self.gradelist = gradelist
        for i in range(0, len(self.courselist)):
            initdict[self.courselist[i]] = self.gradelist[i]
        self.courses_and_grades = initdict
        initlist.append(name)
        self.all_students = initlist
        nonum = 0
        for item in self.courses_and_grades.values():
            nonum += item
        self.average = nonum / len(self.courses_and_grades.values())



    def add_course(self, coursename, coursegrade):
        self.courses_and_grades[coursename] = coursegrade

    def course_grade(self, cname, cgrade):
        all_courses = self.courses_and_grades.keys()
        if cname in all_courses:
            self.courses_and_grades[cname] = cgrade
        else:
            print(f"{self.name} {self.lastname} doesn\'t study {cname}.")

    def sum_courses(self):
        return len(self.courses_and_grades.keys())
    
    def calculate_average(self):
        all_grades = self.courses_and_grades.values()
        sum_grades = 0
        for value in all_grades:
            sum_grades += value
        self.average = sum_grades / len(all_grades)
        return self.average
    
    def number_of_students(self):
        return len(self.all_students)

    def __str__(self):
        return f'Your name is {self.name} {self.lastname}.\nThe courses you take are {', '.join(self.courses_and_grades.keys())}.\nYour average score is {self.average:.2f}.\nThe number of the students is {len(self.all_students)}.'


raz = Student("Raz", "Asraf", 323838110, ["Python", "blatavovich", "SQL"], [100, 10, 30])
raz.add_course("CIcd", 70)
raz.course_grade("anatoly", 50)
print(raz)