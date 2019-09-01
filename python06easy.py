# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self,color,name):
        self.speed = 150
        self.color = color
        self.name = name
        self.is_police = False
    def go(self):
        print('Lets Goooo!')
    def stop(self):
        print('{} has stopped'.format(self.name))
    def turn(self,direction):
        if direction == 'Left':
            print('Turned Left')
        elif direction == 'Right':
            print('Turned Right')
        else:
            print('Invalid direction!')


class SportCar(TownCar):   #Здесь унаследовал все методы от таун кара в остальные классы
    def __init__(self,color,name):
        self.speed = 150
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(TownCar):
    def __init__(self,color,name):
        self.speed = 120
        self.color = color
        self.name = name
        self.is_police = False



class PoliceCar(TownCar):
    def __init__(self,color,name):
        self.speed = 210
        self.color = color
        self.name = name
        self.is_police = True
    
    



Police1 = PoliceCar('blue','Los Angeles Police Department')

Police1.go()

Police1.stop()





# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.