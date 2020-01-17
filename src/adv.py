from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('rusty dagger', 'it looks very old'),
                     Item('loaf of bread', 'why is it sitting out here?')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                [Item('staff', 'or is it just a walking stick?'),
                Item('rope', 'this may come in handy')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                [Item('longbow', 'if only there we some arrows...'),
                Item('quiver of arrows', 'if only there were a bow...')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                [Item('ring', 'did you hear that?'),
                Item('shortsword', 'it\'s still sharp'),
                Item('warm winter cloak', 'goes perfect with a cup of hot chocolate')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                [Item('wrinkly treasure map', 'looks like this was left behind'),
                Item('worn wizard hat', 'it\'s still warm')])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Create a player
# Let player input their name

player = Player(input("What is your name, adventurer?\n "), room['outside'], Item("stick", "yep, a stick").name)
print(f'\nGreetings, {player.name}. Welcome to the land of Adbmal. All you have with you is a stick. Yep, a stick.\n')
print(f'Your current location: {player.current_room.name}. {player.current_room.description}.\n')
print(  'What shall you do, adventurer? \n\n'
        'Type "n" to go north.\n'
        'Type "s" to go south.\n'
        'Type "e" to go east.\n'
        'Type "w" to go west.\n'
        'Type "inventory" to view the items currently in your inventory.\n'
        'Type "pick up <item>" to pick up a specific item.\n'
        'Type "put down <item>" to put down a specific item.\n'
        'Type "help" see this list again.\n')

directions = ['n', 's', 'e', 'w']

# Create basic REPL loop
while True:
    cmd = input('~~> ').lower()
    if cmd in directions:
        player.travel(cmd)
    elif cmd.lower() == 'help':
        print(
            'Type "n" to go north.\n'
            'Type "s" to go south.\n'
            'Type "e" to go east.\n'
            'Type "w" to go west.\n'
            'Type "inventory" to view the items currently in your inventory.\n'
            'Type "pick up <item>" to pick up a specific item\n'
            'Type "put down <item>" to put down a specific item\n'
            'Type "help" see this list again.\n'
        )
    elif cmd.lower() == 'inventory':
        print(player.inventory)
    elif 'pick up' in cmd.lower():
        cmd = cmd.lower()
        cmd = cmd.replace('pick up', '')
        cmd = cmd.replace(' ', '')
        player.pick_up(cmd)
    elif 'put down' in cmd.lower():
        cmd = cmd.lower()
        cmd = cmd.replace('put down', '')
        cmd = cmd.replace(' ', '')
        player.put_down(cmd)
    elif cmd == 'q':
        print('Farewell')
        exit()
    else:
        print('Sorry, I do not understand that command')
