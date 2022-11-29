'''
ordered array
time complexity : O(nlogn)
simple logic 
find middle then check the value and repeat
middle = floor(low+ (high-low)/2)
[low,high)
'''
import math

def BinarySearch(haystack: list, needle: int) -> bool:
    high = len(haystack)
    low = 0
    while low < high:
        middle = math.floor(low + (high - low)//2)
        # print(middle)
        if haystack[middle] == needle:
            return True
        elif haystack[middle] > needle:
            high = middle
        else:
            low = middle + 1
    return False


if __name__ == "__main__":
    l = [21, 23, 3132, 24211]
    print("first test cases::")
    print(BinarySearch(l, 21))
    print(BinarySearch(l, 23))
    print(BinarySearch(l, 3132))
    print(BinarySearch(l, 24211))
    print(BinarySearch(l, 231))
    print(BinarySearch(l, 6757))
    print(BinarySearch(l, 20))
    print("second test cases::")
    lo = [1, 3, 5, 6, 7]
    print(BinarySearch(lo, 1))
    print(BinarySearch(lo, 3))
    print(BinarySearch(lo, 5))
    print(BinarySearch(lo, 6))
    print(BinarySearch(lo, 7))
    print(BinarySearch(lo, 75))
    print(BinarySearch(lo, 9))
