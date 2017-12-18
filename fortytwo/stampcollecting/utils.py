# currency converter
def LSD_to_newpence(l, s, d):
    return ((l*20 + s)*12 + d)

def newpence_to_LSD(newp):
    l = newp//100
    change = newp - l*100
    changed = int(change * (20*12.0/100))
    s = changed//12
    d = changed - s*12
    return "{} pounds {} shillings {} pence".format(l,s,d)
