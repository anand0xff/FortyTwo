from . import utils
print("::: importing PennyBlack class")


class PennyBlack:

    def __init__(self, initstr):
        print("\t::: PennyBlack.__init__" + initstr)
        self.cost = 1  # old penny

    def currentvalue(self, newp):
        print("\t::: PennyBlack self.cost {}d".format(self.cost))
        print("\t::: PennyBlack price today {}".format(utils.newpence_to_lsd(newp)))


if __name__ == "__main__":

    pb = PennyBlack("from PennyBlack.py __main__ ")
    print(pb.currentvalue(5))
