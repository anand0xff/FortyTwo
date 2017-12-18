# DaBeaz recommends rel in-pkg imports
from ..stampcollecting import utils

print("::: imported Lifshitz class")


class Lifshitz:

    def __init__(self, initstr):
        print("\t::: Lifshitz.__init__")
        self.initstr = initstr
        self.damping(initstr)

    @staticmethod
    def writebook(s):
        print("\t::: Lifshitz.writebook " + s)

        price = utils.newpence_to_lsd(5008)
        print("\t::: Price: " + price)

    @staticmethod
    def damping(s):
        print("\t::: Lifshitz.damping() called " + s)


Lifshitz.damping("from Lifshitz.py class execution")

if __name__ == "__main__":

    ll = Lifshitz("init Lifshitz in Lifshitz.py __main__ ")
    ll.writebook("Fluid Dynamics")
    Lifshitz.damping("from Lifshitz.py __main__")
