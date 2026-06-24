import os
import sys


def two_sum(nums,target):
    seen = {} #hash map

    for i, num in enumerate(nums):
        missing = target - num

        if missing in seen:
            return[seen[missing], i]

        seen[num] = i
    return []


def main():
    nums = [2,7,0,5,4,6,3]
    target = 9

    result = two_sum(nums,target)
    print(result)

if __name__ == "__main__":
    main()