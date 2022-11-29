'''
Time Complexity : O(N^2)
after first iter largest will be at end of array.
'''
def BubbleSort(array: list) -> list:
    for i in range(0, len(array)):
        z = len(array) - 1 - i
        for j in range(0, z):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


if __name__ == "__main__":
    l = [342, 234, 234, 324, 878787, 324, 546, 47, 567, 87, 233]
    print(*(BubbleSort(l)))
