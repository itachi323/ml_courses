# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 16:47:45 2018

@author: ITACHI UCHIHA
"""
from animals import dog
reks=dog(n='reks',col=['black'],eyecol=['green'],l=40,w=50)
lasse=dog(n='lasse',col=['gray'],eyecol=['blue'])
print(reks.color,reks.eyecolor,reks.length,reks.weight)
print(lasse.color,lasse.eyecolor,lasse.length,lasse.weight)
reks.run()
lasse.run()