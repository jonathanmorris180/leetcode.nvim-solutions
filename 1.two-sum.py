# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices: dict[int, int] = {}

        print(f"input is {nums}")

        for i, e in enumerate(nums):
            index_to_check = target - e
            if index_to_check in indices:
                return [indices[index_to_check], i]
            indices[e] = i
        return []


# @leet end
