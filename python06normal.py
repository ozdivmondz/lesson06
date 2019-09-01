# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person():
    def __init__(self,health,armor):
        self.health = health
        self.armor = armor
        self.damage = random.randint(1,10)
    def _calculate_damage(self,enemy):
        return self.damage / enemy.armor
    def Attack(self,enemy):
        enemy.health -= self._calculate_damage(enemy)
class Player(Person):
    pass
class Enemy(Person):
    pass

class Game():
    def __init__(self,player,enemy):
        self._player = player
        self._enemy = enemy
    def StartGame(self):
        while self._player.health > 0 and self._enemy.health > 0:
            self._enemy.Attack(self._player)
            self._player.Attack(self._enemy)

            if self._player.health <= 0:
                print('Enemy wins!')
                break

            elif self._enemy.health <= 0:
                print('Player wins!')
                break

p1 = Player(100,10)
e1 = Enemy(90,10)

game = Game(p1,e1)

game.StartGame()

