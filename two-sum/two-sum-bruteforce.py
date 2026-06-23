import os
import sys


def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return []


def main():
    nums = [2,7,0,5,4]
    target = 9

    result = two_sum(nums,target)
    print(result)

if __name__ == "__main__":
    main()