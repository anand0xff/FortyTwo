print("::: importing landau module")

from ..stampcollecting import utils # DaBeaz recommends rel in-pkg imports


def damping(s):
    print("\t::: landau.damping() called " + s)
    

class Lifshitz():

    def __init__(self,initstr):
        print("\t::: landau.Lifshitz.__init__")
        damping(initstr)

    def writebook(self, s):
        print("\t::: landau.Lifshitz.writebook " + s)

        price = utils.newpence_to_LSD(5008)
        print("\t::: Price: " + price)

damping("from landau.py module execution")


if __name__ == "__main__":

    ll = Lifshitz("init Lifshitz in landau.py __main__ ")
    ll.writebook("Fluid Dynamics")
    damping("from landau.py __main__")
