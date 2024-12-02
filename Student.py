from utils import getNumberFromUser, setIndexAndSpacer
from Person import Person


class Student(Person):
    def __init__(
        self,
        id,
        name,
        age,
        field_of_study=None,
        year_of_study=None,
        score_avg=None,
    ):
        super().__init__(id, name, age)
        if field_of_study is None:
            field_of_study = input("Filed of study: ")
        if year_of_study is None:
            year_of_study = getNumberFromUser("Year of study")
        if score_avg is None:
            score_avg = getNumberFromUser("Score average")
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getFieldOfStudy(self):
        return self._field_of_study

    def getYearOfStudy(self):
        return self._year_of_study

    def getScoreAvg(self):
        return self._score_avg

    def getDictionary(self):
        super_dict = super().getDictionary()
        student_dict = {
            "field_of_study": self._field_of_study,
            "year_of_study": self._year_of_study,
            "score_avg": self._score_avg,
        }
        return super_dict | student_dict

    def printStudent(self, index="", end="\n"):
        _, spacer = setIndexAndSpacer(index)

        self.printPerson(index)
        print(f"{spacer}Field of Study: {self._field_of_study}")
        print(f"{spacer}Year of Study:  {self._year_of_study}")
        print(f"{spacer}Score average:  {self._score_avg}", end=end)

    def printMyself(self, index="", end="\n"):
        self.printStudent(index, end)
