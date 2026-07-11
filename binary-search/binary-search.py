import sys
import os

def binary_search(list, item):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low +high) // 2 
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def main():
    list = [1,3,5,6,7,8,9,11,12,14,15,16,24,25,26,27]
    item = 5
    result = binary_search(list,item)
    print(result)

if __name__ == "__main__":
    main()

