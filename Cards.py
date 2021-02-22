#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:30:15 2021

@author: rickysu
"""

import random

class Deck():
    def __init__(self):
        self.values = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
        self.suits = ['diamonds','clubs','hearts','spades']
        
        self.cards = self.set_cards()
        
    def shuffle(self):
        """
        Shuffles self.cards using random.sample
        """
        self.cards = random.sample(self.cards,len(self.cards))
    
    def shuffle2(self):
        """
        Not sure if the first shuffle function is cheating, but if it is, here's
        another way to do it. For each card index, sample a random index and 
        switch the card indices.
        """
        
        for i in range(len(self.cards)):
            random_index = random.randint(0,len(self.cards)-1)
            temp = self.cards[random_index]
            self.cards[random_index] = self.cards[i]
            self.cards[i] = temp
    
    def dealOneCard(self):
        """
        Deals one card from self.cards, WITHOUT replacement.
        Generate a random index, remove the card from that index, return the card
        
        Returns
        -------
        card : Card object 
            a randomly selected Card object from self.cards
        """
        
        if len(self.cards) == 0:
            message = "Whoops! No more cards to draw! Reset the deck using <deck>.reset()"
            raise Exception(message)
        
        self.shuffle()
        random_index = random.randint(0,len(self.cards)-1)
        card = self.cards.pop(random_index)
        
        return card
        
    def set_cards(self):
        """
        Returns
        -------
        cards : list 
            list of Card objects based on the suits and values passed in
        """
        
        cards = []
        for v in self.values:
            for s in self.suits:
                cards.append(Card(v,s))
        
        return cards
    
    def reset(self):
        """
        Reset self.cards
        """
        self.cards = self.set_cards()
    
    def __repr__(self):
        return 'Deck Object: \n{}'.format(self.cards)


class Card():
    def __init__(self, value, suit):
        """
        Parameters
        ----------
        value : str
            str value (i.e. "ace")
        suit : str
            str suit (i.e. "diamonds")
        """
        
        self.value = value
        self.suit = suit
        self.name = "_".join([value,suit])
    
    def __repr__(self):
        return 'Card Object {}'.format(self.name)
    
    
if __name__ == "main":
    d = Deck()
    
    # This should break
    for _ in range(52):
        d.dealOneCard()
    d.dealOneCard()
    
    # # # Reset the deck
    d.reset()
    
    # This should break again
    for _ in range(52):
        d.dealOneCard()
    d.dealOneCard()