#! /usr/bin/env python

from fortytwo.physics.Lifshitz import Lifshitz
from fortytwo.physics import electron
from fortytwo.stampcollecting import PennyBlack


def hotcuppatea(s):
    print("  ::: hotcuppatea called " + s)


if __name__ == "__main__":

    hotcuppatea("from run42.py __main__")
    davidovich = Lifshitz("from above Physics/")
    davidovich.writebook("Classical Theory of Fields")
    electron.mass()

    pb = PennyBlack.PennyBlack("from driver ")
    pb.currentvalue(300077)
