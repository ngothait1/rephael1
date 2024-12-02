from utils import getNumberFromUser, setIndexAndSpacer
from Person import Person


class Employee(Person):
    def __init__(self, id, name, age, field_of_work=None, salary=None):
        super().__init__(id, name, age)
        if field_of_work is None:
            field_of_work = input("Filed of work: ")
        if field_of_work is None:
            salary = getNumberFromUser("Salary")
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOfWork(self):
        return self._field_of_work

    def getSalary(self):
        return self._salary

    def getDictionary(self):
        super_dict = super().getDictionary()
        employee_dict = {
            "field_of_work": self._field_of_work,
            "salary": self._salary,
        }
        return super_dict | employee_dict

    def printEmployee(self, index="", end="\n"):
        _, spacer = setIndexAndSpacer(index)

        self.printPerson(index)
        print(f"{spacer}Field of Work: {self._field_of_work}")
        print(f"{spacer}Salary:        {self._salary}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printEmployee(index, end)
