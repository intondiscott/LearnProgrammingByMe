"""
Here we will learn how to create and use classes in python
You will learn getters/setters and object inheritance
"""


# create class by using class keyword followed by class name with first letter being uppercase
class Person:
    # constructor gives requirements for making said class, use default attributes to create a class without params
    def __int__(self, name: str = "not specified", age: int = 0, gender: str = "not specified"):
        # use self keyword followed by variable in constructor and set to variable
        self.name = name
        self.age = age
        self.gender = gender

    # setter
    def set_name(self, name: str):
        # use error checking to make sure correct type is used in setting method
        try:
            if type(name) == str:
                Person.name = name
            else:
                raise TypeError
        except TypeError:
            print(f" {Person.set_name} needs to be a string not a {type(name)}")
            Person.name = "not specified"

    # getter
    def get_name(self) -> str:
        return self.name

    # setter
    def set_age(self, age: int):
        try:
            if type(age) == int:
                Person.age = age
            else:
                raise TypeError

        except TypeError:
            print(f" {Person.set_age} needs to be a integer not a {type(age)}")
            Person.age = 0

    # getter
    def get_age(self) -> int:
        return self.age

    # setter
    def set_gender(self, gender: str):
        try:
            if gender == 'male' or 'female':
                Person.gender = gender
            else:
                raise ValueError

        except ValueError:
            print(f" {Person.set_gender} needs to be (male or female) not ({gender})")
            Person.gender = 'not specified'

    # getter
    def get_gender(self) -> str:
        return self.gender

    # return all info of created object
    def get_person_info(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}")


# inheritance
class Employee(Person):
    # use super to copy constructor of class you are inheriting from
    def __init__(self, job_title: str = "not specified", email_address: str = "not specified"):
        super(Person).__init__()
        self.job_title = job_title
        self.email_address = email_address

    def set_job_title(self, job_title: str):
        try:
            if type(job_title) == str:
                self.job_title = job_title
            else:
                raise TypeError

        except TypeError:
            print(f" {Employee.set_job_title} needs to be a string not a {type(job_title)}")
            self.job_title = "not specified"

    def get_job_title(self) -> str:
        return self.job_title

    def set_email_address(self, email_address: str):
        try:
            if type(email_address) == str and email_address.__contains__("@"):
                self.email_address = email_address
            else:
                raise TypeError and ValueError

        except TypeError and ValueError:
            print(f" {Employee.set_email_address} needs to be a string not a {type(email_address)} and contain (@) "
                  f"for valid email")
            self.email_address = "not specified"

    def get_email_address(self) -> str:
        return self.email_address

    def get_all_info(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}, job title: {self.job_title}, "
              f"email address: {self.email_address}")


def main():
    # normal object
    person = Person()
    person.set_name("john"), person.set_age(40), person.set_gender('male')
    person.get_person_info()

    # object 1 inheritance
    em1 = Employee()
    em1.set_name("Scotty"), em1.set_age(37), em1.set_gender("male")
    em1.set_email_address("Scotty@gmail.com"), em1.set_job_title("software Engineer")
    em1.get_person_info()
    em1.get_all_info()

    # object 2 inheritance
    em2 = Employee()
    em2.set_name("lisa"), em2.set_age(34), em2.set_gender("female")
    em2.set_email_address("lisa@gmail.com"), em2.set_job_title("sales rep")
    em2.get_all_info()


if __name__ == "__main__":
    main()
