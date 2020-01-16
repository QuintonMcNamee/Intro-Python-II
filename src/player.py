# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, hp):
        self.name = name
        self.room = room
        self.hp = hp
    
class Warrior(Player):
    def __init__(self, name, room, hp=10):
        super().__init__(name, room, hp)
    def attack(self):
        print('Attack!')
    def desc(self):
        print('Player with high health and melee abilities')

class Mage(Player):
    def __init__(self, name, room, hp=6):
        super().__init__(name, room, hp)
    def attack(self):
        print('Fireball!')
    def desc(self):
        print('Player with medium health and powerful ranged abilities')

class Priest(Player):
    def __init__(self, name, room, hp=4):
        super().__init__(name, room, hp)
    def heal(self):
        print('Renew!')
    def desc(self):
        print('Player with low health but powerful healing abilities')

q = Warrior('Quinton', 'outside')
b = Mage('Bob', 'foyer')
e = Priest('El', 'overlook')