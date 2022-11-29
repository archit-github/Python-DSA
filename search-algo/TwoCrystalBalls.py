'''
problem statement: [f,f,f,f,f,t,t,t,t,t]
find first t only have two chances to  choose correct and return index.
first approach : iterate over array. O(N)
second approach : iterate sqrt(N) over array then find t and go back one step back and linear search that.
'''
import math
def TwoCrystalBalls(basket: list)-> int:
    jmpAmt = math.floor(math.sqrt(len(basket)))
    index = 0
    for i in range(0, len(basket), jmpAmt):
        if basket[i]:
            index = i
            break
    lowIndex = index - jmpAmt
    if lowIndex < 0: 
        lowIndex = 0
    for i in range(lowIndex, len(basket)):
        if basket[i]:
            return i 
    return -1


if __name__ == "__main__":
    l = [False, False, False, False,False, True,True,True,True,True]
    print(TwoCrystalBalls(l))
    lo = [True,True,True,True,True]
    print(TwoCrystalBalls(lo))
    low = [False, False, False, False,False,True]
    print(TwoCrystalBalls(low))