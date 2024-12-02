from utils import setIndexAndSpacer

class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getType(self):
        return self.__class__.__name__

    def getDictionary(self):
        return {
            "id": self._id,
            "name": self._name,
            "age": self._age,
        }

    def printPerson(self, index="", end="\n"):
        pre_id, spacer = setIndexAndSpacer(index)

        print(f"{pre_id}Type: {self.getType()}")
        print(f"{spacer}ID:   {self._id}")
        print(f"{spacer}Name: {self._name}")
        print(f"{spacer}Age:  {self._age}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printPerson(index, end)
