'''
time complexity : O(N)
iterate over each value and return.
'''

def LinearSearch(array: list, value: int) -> bool:
    for i in array:
        if i == value:
            return True
    return False


if __name__ == "__main__":
    l = [31,123,231,213,123,321]
    print(LinearSearch(l, 3))
    print(LinearSearch(l, 31))
    print(LinearSearch(l, 123))
    print(LinearSearch(l, 332))
    print(LinearSearch(l, 323))
    print(LinearSearch(l, 321))
