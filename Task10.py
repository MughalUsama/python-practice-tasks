

class Person:
    """
    A Class to Store Details of a Person
    """
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def getGender(self):
        return "Not Specified"

    def display_name(self):
        print(self.first_name, self.last_name)


class Male(Person):
    """
    A Class to Store Details of a Male Person
    """
    __gender = "Male"

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)

    def getGender(self):
        return self.__gender


class Female(Person):
    """
    A Class to Store Details of a Female Person
    """
    __gender = "Female"

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)

    def getGender(self):
        return self.__gender


if __name__ == "__main__":
    person = Person("Abc", "XYZ")
    person.display_name()
    print("Gender:", person.getGender())

    person1 = Male("ALI", "PQR")
    person1.display_name()
    print("Gender:", person1.getGender())

    person2 = Female("ZXY", "XYZ")
    person2.display_name()
    print("Gender:", person2.getGender())
