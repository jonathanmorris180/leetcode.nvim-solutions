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
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        indices: dict[int, int] = {}

        for i, e in enumerate(nums):
            idx = target - e
            if idx in indices:
                return [indices[idx], i]
            indices[e] = i

        return []


# @leet end
