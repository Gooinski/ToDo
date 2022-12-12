# class Card:
# hold a card
# matched or not?
# location on the game board
# __eq__
# __str__ what to display to player

class Card:
    def __init__(self, word, location) -> None:
        self.card = word
        self.location = location
        self.matched = False

    def __eq__(self, other) -> bool:
        return self.card == other.card

    def __str__(self) -> str:
        return self.card

if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('dog', 'C1')

    print(card1 == card2)
    print(card2 == card3)
    print(card3)