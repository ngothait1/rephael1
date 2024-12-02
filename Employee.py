from utils import isDigit
from Person import Person


class Employee(Person):
    def __init__(
        self, id, name, age, field_of_work=None, salary=None, user_input=False
    ):
        if user_input:
            field_of_work = input("Filed of work: ")
            while True:
                salary = input("Salary: ")
                if isDigit(salary, "Salary"):
                    salary = int(salary)
                    break
        super().__init__(id, name, age)
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
        if index != "":
            spacer = len(index) * " " + "  "
        else:
            spacer = ""

        self.printPerson(index)
        print(f"{spacer}Field of Work: {self._field_of_work}")
        print(f"{spacer}Salary:        {self._salary}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printEmployee(index, end)
