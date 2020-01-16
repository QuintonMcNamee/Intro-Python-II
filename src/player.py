# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, hp):
        self.name = name
        self.current_room = starting_room
        self.hp = hp
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('You cannot move in that direction')
    
class Warrior(Player):
    def __init__(self, name, starting_room, hp=10):
        super().__init__(name, starting_room, hp)
    def travel(self, direction):
        super().travel(direction)
    def attack(self):
        print('Attack!')
    def desc(self):
        print('Player with high health and melee abilities')

class Mage(Player):
    def __init__(self, name, room, hp=6):
        super().__init__(name, room, hp)
    def travel(self, direction):
        super().travel(direction)
    def attack(self):
        print('Fireball!')
    def desc(self):
        print('Player with medium health and powerful ranged abilities')

class Priest(Player):
    def __init__(self, name, room, hp=4):
        super().__init__(name, room, hp)
    def travel(self, direction):
        super().travel(direction)
    def heal(self):
        print('Renew!')
    def desc(self):
        print('Player with low health but powerful healing abilities')

q = Warrior('Quinton', 'outside')
b = Mage('Bob', 'foyer')
e = Priest('El', 'overlook')