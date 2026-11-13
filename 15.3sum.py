# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
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
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Approach for this is to use three pointers
        # The leftmost pointer will just iterate through the array
        # unless the previous element is the same as the current
        # The other two pointers will act as they do in Two Sum II (sorted array)

        # IMPORTANT: You have to continue looking for all possible
        # results even after a target has been found for nums[i]
        # so if nums[i] is -1 and you find a solution, you need to
        # keep searching for another solution, keeping i on -1

        nums.sort()

        ans = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i - 1] == num:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    r -= 1
                    # Don't actually need to incement l here
                    # since on the next iteration, the sum will be negative
                    # (num and nums[l] will be the same value, but
                    # nums[rNew] will be less due to the array being sorted).
                    # Since the next value is negative, the `elif total < 0` branch
                    # will fire, incrementing l
                    while r > l and nums[r + 1] == nums[r]:
                        r -= 1

        return ans


# @leet end
