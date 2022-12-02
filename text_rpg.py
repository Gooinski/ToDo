# playerDict = {
#     'name':'Chris',
#     'class':'Tech',
#     'species':'Human',
#     'level': 1,
#     'Strength': 8,
#     'Intelligence': 6,
#     'Dexterity': 5,
#     'Constition': 9,
#     'Charisma': 4,
# }

# playerDict['name'] = 'Bob'
# playerDict['Strength'] = playerDict['Strength'] + 5
# playerDict['Experience'] = 10

# print(playerDict['Experience'])
# print(playerDict['Strength'])
# print(playerDict['name'])

# playerDict['Experience'] += 10

# print(playerDict['Experience'])

class player:
    def __init__(
        self,
        name: str,
        char_class: str,
        species: str,
        level: int,
        strength: int,
        intelligence: int,
        dexterity: int,
        constitution: int,
        charisma: int,
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

player1 = player('Chris','Warrior','Human',43,8,8,7,10,4,)
player2 = player('Ben', 'Rogue', 'Human',7,6,9,10,5,11,)

print(
    player1.name,
    player1.level,
    player2.name,
    player2.level)
