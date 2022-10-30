# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:56:17 2022

@author: Landon, Alvin, Aidan
"""

#graph 1
g = {
     'A': set(['B', 'E', 'F']),
     'B': set(['A', 'C', 'E']),
     'C': set(['B', 'D', 'G']),
     'D': set(['C', 'G']),
     'E': set(['A', 'F', 'I']),
     'F': set(['A','B', 'E', 'I']),
     'G': set(['C', 'D', 'J']),
     'H': set(['K', 'L']),
     'I': set(['E', 'F', 'J', 'M']),
     'J': set(['G', 'I']),
     'K': set(['H', 'L', 'O']),
     'L': set(['H', 'K', 'P']),
     'M': set(['I', 'N']),
     'N': set(['M']),
     'O': set(['K']),
     'P': set(['L']),
    }

#graph 2
g2 = {
     '1': set(['3']),
     '2': set(['1']),
     '3': set(['2', '5']),
     '4': set(['1', '2', '12']),
     '5': set(['6', '8']),
     '6': set(['7','8','10']),
     '7': set(['10']),
     '8': set(['9', '10']),
     '9': set(['5', '11']),
     '10': set(['9', '11']),
     '11': set(['12']),
     '12': set([]),
}

#graph 3