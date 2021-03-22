import tkinter as tk
from random import shuffle

#root = tk.Tk()

SCORE_TABLE = {'6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'Валет♠': 2, 'Дама♠': 3, 'Король♠': 4, 'Туз♠': 11,
                '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'Валет♥': 2, 'Дама♥': 3, 'Король♥': 4, 'Туз♥': 11,
                '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'Валет♣': 2, 'Дама♣': 3, 'Король♣': 4, 'Туз♣': 11,
                '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'Валет♦': 2, 'Дама♦': 3, 'Король♦': 4, 'Туз♦': 11}

class Deck():
    def __init__(self):
        self.consist = ['6♠', '7♠', '8♠', '9♠', '10♠', 'Валет♠', 'Дама♠', 'Король♠', 'Туз♠',
                        '6♥', '7♥', '8♥', '9♥', '10♥', 'Валет♥', 'Дама♥', 'Король♥', 'Туз♥',
                        '6♣', '7♣', '8♣', '9♣', '10♣', 'Валет♣', 'Дама♣', 'Король♣', 'Туз♣',
                        '6♦', '7♦', '8♦', '9♦', '10♦', 'Валет♦', 'Дама♦', 'Король♦', 'Туз♦']
        self.shuffle()

    def shuffle(self):
        '''Перемешивает карты'''
        return shuffle(self.consist)

    def pop(self):
        return self.consist.pop()

    def __repr__(self):
        return str(self.consist)
    
        

class Hand(Deck):
    def __init__(self, player):
        self.consist = []

    def __add__(self, other):
        return self.consist + [other]

class Player():
    def __init__(self, player=0):
        self.player = player
        self.hand = Hand(player)
        self.scores = 0

    def turn(self):
        card = deck.pop()
        self.hand += card
        self.scores += SCORE_TABLE[card]
        


deck = Deck()
a = Player()

