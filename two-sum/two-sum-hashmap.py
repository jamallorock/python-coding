import os
import sys


def two_sum(nums,target):
    seen = {} #hash map

    for i, num in enumerate(nums):
        missing = target - num
        print(missing)
        if missing in seen:
            print(missing)
            return[seen[missing], i]

        seen[num] = i
    return []


def main():
    nums = [2,7,0,5,4,6,3]
    target = 12

    result = two_sum(nums,target)
    print(result)

if __name__ == "__main__":
    main()