# Quick Sort Algorithm
# This program is intended to take in a set of numbers and sort them in ascending order.
# written by Carter Pon
# source: geeksforgeeks.org/quick-sort/

import random

nums = []


def populate():
    for x in range(11):
        nums.put(random.randint(1, 100))
    print(nums)


def quicksort():

