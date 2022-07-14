# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:02:14 2022

@author: 17066
"""

import numpy as np
import dominionSolver.objects as dso

class game():
    """Object Tracking all cards in the game"""
    
    def init(self,nPlayers,field):
        """Initialize the game
        
        parameters
        ----------
        nPlayers - integer
            number of players in the game
        field - list of integers
            list of card Ids, specifying which cards are on the field are on 
            the field
        
        """
        
        self.nPlayers = nPlayers
        
        self.field = {}
        for Id in field:
            self.field[Id] = library[Id]
    
    def buy(self,card):
        if self.card()