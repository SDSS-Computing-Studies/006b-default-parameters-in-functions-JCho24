#! python3

import math


def tempConversion(deg, unit="F"):
    if unit == "C":
        ans = (deg * (9/5) + 32)
    
    elif unit == "F":
        ans = ((deg - 32) * (5/9))
        
    ans = round(ans,1)
    return ans

def factorPair(number, factor):
    fpair = number / factor
    
    pairlist = [int(factor), int(fpair)]
    pairlist.sort()

    return pairlist

def toRadians(degree):
    radians = (degree * math.pi)/180
    return radians

def solution(sol):
    quadanswer = sol[1]
    return quadanswer

def quadratic(a,b,c):
    if b**2 > 4*a*c:
        ans1a = math.sqrt((b**2) - (4 * a * c))
        ans1b = 2*a
        ans1 = (-b + ans1a) / ans1b

        ans2a = math.sqrt((b**2) - (4 * a * c))
        ans2b = 2*a
        ans2 = (-b - ans2a) / ans2b


        quadlist = [ans1,ans2]
        quadlist.sort()
        quadanswer = quadlist
        return quadanswer


def cosineLaw(s1,s2,angle3,oppositeSide=True):
    s3a = (s1**2) + (s2**2)
    s3b = (2 * s1 * s2 * math.cos(toRadians(angle3)))
    s3 = s3a - s3b
    s3 = math.sqrt(s3)

    if oppositeSide == False:
        if s1 > s2:
            lnum = s1
            snum = s2

        else:
            lnum = s2
            snum = s1

        q1 = 1
        q2 = -2*snum*math.cos(toRadians(angle3))
        q3 = (snum**2) - (lnum**2)
        x = quadratic(q1,q2,q3)
        y = solution(x)
        return y

    
    return s3

    
Cosine_assignment = cosineLaw(10,3,50,oppositeSide=False)
print(Cosine_assignment)

quadratic_assignment = quadratic(3,5,-8)
print(quadratic_assignment)

solution_assignment = solution(quadratic_assignment)
print(solution_assignment)