from person import Person

class Student(Person):
    def __init__(self, name, age, school):
        # super()函式將使子類別繼承其父類別的所有方法和屬性：https://www.w3schools.com/python/python_inheritance.asp
        super().__init__(name, age)
        self.school = school

    # 刪除重複的函式

    def print_school(self):
        print(self.school)