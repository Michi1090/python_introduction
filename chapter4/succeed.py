class animalBaseClass:
    animal_legs = 4

    def walk(self):
        print('歩く')

    def cry(self):
        print('鳴く')

    def getLegsNum(self):
        print(self.animal_legs)


class dogClass(animalBaseClass):
    def __init__(self):
        print('犬です')


wanko = dogClass()
wanko.walk()
wanko.cry()
wanko.getLegsNum()


class catClass(animalBaseClass):
    def __init__(self):
        print('猫です')

    def cry(self):
        print('にゃー')


nyanko = catClass()
nyanko.walk()
nyanko.cry()
