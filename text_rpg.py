playerDict = {
    'name':'Chris',
    'class':'Tech',
    'species':'Human',
    'level': 1,
    'Strength': 8,
    'Intelligence': 6,
    'Dexterity': 5,
    'Constition': 9,
    'Charisma': 4,
}

for key, value in playerDict.items():
    print(key)
    print(value)

print(len(playerDict))

# playerDict['name'] = 'Bob'
# playerDict['Strength'] = playerDict['Strength'] + 5
# playerDict['Experience'] = 10

# print(playerDict['Experience'])
# print(playerDict['Strength'])
# print(playerDict['name'])

# playerDict['Experience'] += 10

# print(playerDict['Experience'])
class Char_Class:
    def __init__(self) -> None:
        self.char_class_list =["Warrior", "Rogue", "Mage", "Priest", "Paladin", "Pirate", "Ninja", "NPC"]

    def __iter__(self):
        yield from self.char_class_list

class Player():
    def __init__(
        self,
        name: str,
        char_class="X",
        species='Human',
        level=1,
        strength=5,
        intelligence=5,
        dexterity=5,
        constitution=5,
        charisma=5,
        experience=0,
    ) -> None:
        self.name = name
        self.char_class = char_class
        self.species = species
        self.level = level
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.constitution = constitution
        self.charisma = charisma
        self.experience = experience
    
    def __str__(self) -> str:
        return f'{self.name}, {self.char_class}, {self.level}'

    def attack(self):
        print(f'{self.name} Attacks!')

    def block(self):
        print(f'{self.name} Blocks!')

player1 = Player('Chris','Warrior','Human',43,8,8,7,10,4,)
player2 = Player('Ben', 'Rogue', 'Human',7,6,9,10,5,11,)
player3 = Player('Kim')

print(
    player1.name, '\n',
    player1.level, '\n',
    player2.name, '\n',
    player2.level, '\n',
    player3,
    )

player1.attack()
player2.block()

my_char_class = Char_Class()

for attribute in my_char_class:
    print(attribute)

print(dir(my_char_class))