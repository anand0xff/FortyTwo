#! /usr/bin/env python

from fortytwo.physics import electron, landau
from fortytwo.stampcollecting import oldstamps 

def hotcuppatea(s):
    print("  ::: hotcuppatea called " + s)

if __name__ == "__main__":

    hotcuppatea("from run42.py __main__")
    davidovich = landau.Lifshitz("from above Physics/")
    davidovich.writebook("Classical Theory of Fields")
    electron.mass()

    pb = oldstamps.PennyBlack("from driver ")
    pb.currentvalue(300077)
