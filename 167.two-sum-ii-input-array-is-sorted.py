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
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # Should be able to use two pointers for this
        # Probably can start at either end of the array
        # and contract the window based on the target
        # since it's already sorted

        # If the target is less, decrease the right pointer
        # If the target is more, increase the left pointer

        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            res = numbers[l] + numbers[r]
            if target < res:
                r -= 1
            elif target > res:
                l += 1
            else:
                return [l + 1, r + 1]

        return [l + 1, r + 1]


# @leet end
