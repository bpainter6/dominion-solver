# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 23:03:31 2022

@author: 17066
"""

import dominionSolver.objects as dso
import pickle
import os

# Tells the field how many cards should populate each card stack
library = {0  : [dso._Adventurer  , "adventurer"  , 10],
           1  : [dso._Bureaucrat  , "bureaucrat"  , 10],
           2  : [dso._Cellar      , "cellar"      , 10],
           3  : [dso._Chancellor  , "chancellor"  , 10],
           4  : [dso._Chapel      , "chapel"      , 10],
           5  : [dso._Council_room, "council room", 10],
           6  : [dso._Copper      , "copper"      , 60],
           7  : [dso._Feast       , "feast"       , 10],
           8  : [dso._Festival    , "festival"    , 10],
           9  : [dso._Laboratory  , "laboratory"  , 10],
           10 : [dso._Library     , "library"     , 10],
           11 : [dso._Market      , "market"      , 10],
           12 : [dso._Militia     , "militia"     , 10],
           13 : [dso._Mine        , "mine"        , 10],
           14 : [dso._Moat        , "moat"        , 10],
           15 : [dso._Money_lender, "money lender", 10],
           16 : [dso._Remodel     , "remodel"     , 10],
           17 : [dso._Silver      , "silver"      , 40],
           18 : [dso._Smithy      , "smithy"      , 10],
           19 : [dso._Spy         , "spy"         , 10],
           20 : [dso._Thief       , "thief"       , 10],
           21 : [dso._Throne_room , "throne room" , 10],
           22 : [dso._Village     , "village"     , 10],
           23 : [dso._Witch       , "witch"       , 10],
           24 : [dso._Curse       , "curse"       , 30],
           25 : [dso._Woodcutter  , "woodcutter"  , 10],
           26 : [dso._Workshop    , "workshop"    , 10],
           27 : [dso._Duchy       , "duchy"       , 12],
           28 : [dso._Gardens     , "gardens"     , 12],
           29 : [dso._Province    , "province"    , 12],
           30 : [dso._Estate      , "estate"      , 24],
           31 : [dso._Gold        , "gold"        , 30]}

default_games = {"setup"           : [ 6,17,27,29,30,31],
                 "First Game"      : [ 2,11,12,13,14,16,18,22,25,26],
                 "Big Money"       : [ 0, 1, 3, 4, 7, 9,11,13,15,21],
                 "Interaction"     : [ 1, 3, 5, 8,10,12,14,19,20,22],
                 "Size Distortion" : [ 2, 4, 7,28, 9,20,22,23,25,26],
                 "Village Square"  : [ 1, 2, 8,10,11,16,18,21,22,25]}

"""
The actionDict is a preallocated dictionary of all possible rewards a card can
give to a player for using the card

keys
----
"treasure"
    player gains n points of treasure for that round
"buy"
    player gains n buy actions for that round
"action"
    player gains n actions for that round
"gain card"
    player gains a card worth a value up to n treasure points
"trash treasure"
"""

card_actions = {"treasure"       : 0,
                "buy"            : 0,
                "action"         : 0,
                "gain card"      : 0,
                "trash treasure" : 0,
                "moat"           : False}

base_path = os.relpath(r'\dominion-solver')

with open(base_path+r'data\library.pkl', 'wb') as f:
    pickle.dump(library, f)

with open(base_path+r'data\default_games.pkl', 'wb') as f:
    pickle.dump(default_games, f)

with open(base_path+r'data\card_actions.pkl', 'wb') as f:
    pickle.dump(card_actions, f)