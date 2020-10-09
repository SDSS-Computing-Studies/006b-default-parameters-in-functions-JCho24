#! python3

import math


def tempConversion(deg, unit="fc"):
    if unit == "cf":
        ans = (deg * (9/5) + 32)
    
    elif unit == "fc":
        ans = ((deg - 32) * (5/9))
        
    ans = round(ans,1)
    return ans

def factorPair(number, factor):
    fpair = number / factor
    
    pairlist = [int(factor), int(fpair)]
    pairlist.sort()

    return pairlist

def cosineLaw():
    pass
def toRadians():
    pass
def solution():
    pass
def quadratic():
    pass    

