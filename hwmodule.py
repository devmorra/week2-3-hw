from math import pi, fabs
# I'm just converting negative numbers into positive because I don't want to write ValueError cases too
def getCircleArea(r):
    if not isinstance(r, int) or not isinstance(r, float):
        raise TypeError("give number to getCircleArea")
    return pi * fabs(r) **2

def getSquareFootage(l, w):
    if not isinstance(l, int) or not isinstance(l, float) or not isinstance(w, int) or not isinstance(w, float):
        raise TypeError("length and width input should be number for getSquareFootage thanks")
    return fabs(l) * fabs(w)