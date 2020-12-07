class Person:
    def __init__(self, vname, zname):
        self.vname = vname
        self.zname = zname

    def get_info(self):
        return f'{self.vname} {self.zname}'

class Student(Person):
    def get_info(self):
        return f'Student {self.vname} {self.zname}'

class Lektor(Person):
    def __init__(self, vname, zname, fachbereich):
        super().__init__(vname, zname)
        self.fachbereich = fachbereich

    def get_info(self):
        return f'Lektor {self.vname} {self.zname} in Fachbereich {self.fachbereich}'

class Mentor(Lektor):
    def get_info(self):
        return f'{self.zname} Sensei'

if __name__ == '__main__':
    bunch_of_people = []
    bunch_of_people.append(Person("Hansi", "Hinterseer"))
    bunch_of_people.append(Student("Maria", "Musterstudi"))
    bunch_of_people.append(Lektor("Sandra", "Schuster", "Data Science"))
    bunch_of_people.append(Mentor("Kurti", "Muster", "Informatik"))

    for p in bunch_of_people:
        print(p.get_info())



