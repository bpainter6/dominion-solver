# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:52:13 2022

@author: 17066
"""

import numpy as np
import dominionSolver.objects as dso

class player():
    """Broad class for describing player actions"""
    
    def init(self):
        self.deck = []
        self.discard = []
    
    def playTurn(self):
    
class realPlayer(dso.player):
    """Object describing a player who makes decisions via the UI"""
    
    def init(self,typ="action"):
        
        self.typ = typ
        self.


class neuralPlayer(dso.player):
    """Object describing a plyer who makes decisions via neural networks"""
    
    def init(self,neuralDict):
        
        self.neuralDict = neuralDict
    
    
    
    def state(self):
        """Tracks the state of a player up until their turn"""
        self.