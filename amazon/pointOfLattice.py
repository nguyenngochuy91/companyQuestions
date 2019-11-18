# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:26:55 2019

@author: huyn
"""
"""
Point of Lattice"""
def findLattice(AX,AY,BX,BY):
    if AX == BX: # traverse parallel to y axis so basically depends on BY
        if AY>BY: # going top to bot, turn right means decrement x
            return "{},{}".format(AX-1,BY)
        else: # going bot to top, turn right means increment x
            return "{},{}".format(AX+1,BY)
    else:
        # calculate vector AB
        ab = (BX-AX,BY-AY)
        # vector bk = (KX-BX,KY-BY)
        # turn right means ab.bk = 0
        # let a = BX-AX,b = BY-AY, c = BX, d = BY
        a = BX-AX
        b = BY - AY
        c = BX
        d= BY
        # Kx*c + Ky*d = ac + bd
        # find Kx,Ky so that we have integer solution and the smallest distance
        
    return