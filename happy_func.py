from gain_formula import train

# % bonus training paramenters
PERKS = [0.02, 0.1]#, 0.1, 0.01]

HAPPY = 5025
BOOSTER_CD = 24


##########  TRAINING STRATEGIES ##############
def _time_xtrain(stat_fin, stat_ini , happy=HAPPY, refill=True):
    h = 0
    stat_last = stat_ini
    while (stat_ini < stat_fin):
        x = train(happy, stat_ini, 1500/24) # entrenamos 1500 E/dia cada 8 horas, 3 veces al día
        h += 1 
        stat_last = stat_ini
        stat_ini = x["stat"]
    h = h - 1 + (stat_fin - stat_last)/(stat_ini-stat_last)
    return h
#######################################################
########### BYNARY SEARCH ################
def _binsearch(func, ytarget, xmin=0, xmax=1e6):
    ymin = func(xmin)
    ymax = func(xmax)
    if ymax < ytarget or ymin > ytarget:
        #raise ValueError(f"target range out of bounds: {ytarget} is not in [{ymin},{ymax}]")
        print(f"target range out of bounds: {ytarget} is not in [{ymin},{ymax}]")
    xnew = (xmax + xmin)/2
    ynew = func(xnew)
    while abs(xmax - xmin) > 0.01:
        xnew = (xmax + xmin)/2
        ynew = func(xnew)
        if ynew < ytarget:
            xmin = xnew
        elif ynew > ytarget:
            xmax = xnew
    return {"x": xnew,
            "y": ynew,
            "target": ytarget}

def f_days(happy, stat, refill=True):
    jump = train(happy, stat, 1150 if refill else 1000)
    stat_fin = jump["stat"]
    xtrain = _time_xtrain(stat_fin, stat, HAPPY, refill)
    return (xtrain - 32)/24


def f_happy(days, stat, refill=True):
    def f(happy):
        return f_days(happy, stat, refill)
    res = _binsearch(f, ytarget=days, xmin=0, xmax=99999*2)
    return res["x"]

def f_stat(days, happy, refill=True):
    def g(stat):
        return f_happy(days, stat, refill)
    res = _binsearch(g, ytarget=happy, xmin=0, xmax=10e6)
    return res["x"]