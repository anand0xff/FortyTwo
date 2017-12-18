from . import utils
print("::: importing oldstamps module")

class PennyBlack():

    def __init__(self, initstr):
        print("\t::: oldstamps.PennyBlack.__init__" + initstr)
        self.cost = 1 # old penny

    def currentvalue(self, newp):
        print("\t::: PennyBlack self.cost {}d".format(self.cost))
        print("\t::: PennyBlack price today {}".format(utils.newpence_to_LSD(newp)))

if __name__ == "__main__":

    pb = PennyBlack("from oldstamps.py __main__ ")
    print(pb.currentvalue(5))
