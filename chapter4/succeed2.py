class animalBaseClass():
    def __init__(self, num):
        self.animal_legs = num

    def walk(self):
        print('歩く')

    def cry(self):
        print('鳴く')

    def getLegsNum(self):
        print(self.animal_legs)


class snakeClass(animalBaseClass):
    def __init__(self, num):
        super().__init__(num)
        print('蛇です')


nyoro = snakeClass(0)
nyoro.getLegsNum()
