# @leet imports start
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # For this, we can compute the time to the finish for each fleet
        # and see if they will outpace each other

        # First, we need the fleets in sorted, reversed order
        # So, we can always guarantee that the fleet to the left
        # is ahead of the fleet to the right
        fleets = [(position[i], speed[i]) for i in range(len(position))]

        fleets.sort(reverse=True)

        # We could use a stack here to avoid multiple for loops... stack solution below

        # stack = []
        # for p, s in fleets:  # Reverse Sorted Order
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)

        # Compute the times to finish
        times = []
        ans = 0

        for fleet in fleets:
            # time = distance / speed
            pos, sp = fleet
            time = (target - pos) / sp
            times.append(time)

        prevTime = 0
        for time in times:
            if time > prevTime:
                ans += 1
                prevTime = time

        return ans


# @leet end
