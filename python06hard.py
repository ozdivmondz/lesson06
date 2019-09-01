# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
 
# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class BeginManufacturing():
    def __init__(self,name,color,type_of):
        self.name = name
        self.color = color
        self.type = type_of
    def sending_to_production(self):
        print('{} , {} , {} , is sent to prodution'.format(self.color,self.name,self.type))


class Animal(BeginManufacturing):
    pass
class Character(BeginManufacturing):
    pass


class PurchaseOfMaterial(BeginManufacturing):
    def __init__(self):
        super().__init__()
        print('Purchasing material')
    def Color_of_material(self):
        print('purchasing {} material'.format(self.color))

class Sewing(PurchaseOfMaterial):
    def __init__(self):
        super().__init__()
        print('Sewing')
    def Sewing_name_onto_product(self):
        print('Printing {} onto product'.format(self.type))
    

class PaintJob(Sewing):
    def __init__(self):
        super().__init__()
        print('Painting {} color'.format(self.color)
    def _if_character(self):
        if self.type == 'Character':
            print('printing a picture of {}'.format(self.name))
    def caution_label(self):
        print('Adding a CAUTION label onto product')
    
class Shipment(PaintJob):
    def __init__(self):
        super().__init__()
        print('Shipping {}, a {} colored {}'.format(self.name,self.color,self.type))
        return class Ready_Product(PaintJob):
            print('A product has been manufactured and shipped to local dealer')

Toy1 = BeginManufacturing('spider man','red','Character')


