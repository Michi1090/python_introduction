class staff:
    def __init__(self, bonus):
        self.bonus = bonus

    def salary(self):
        salary = 10000 + self.bonus
        return salary

yamamoto = staff(50000)
print(yamamoto.salary())


class staffInfo:
    def __init__(self, staff_id):
        self.staff_id = staff_id

    def getWorkHours(self):
        pass

    def getHireDate(self):
        pass

    def getTraningRank(self):
        pass

tanaka = staffInfo('A00122')
