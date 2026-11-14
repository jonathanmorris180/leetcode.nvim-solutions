# @leet imports start
import bisect
import collections
import copy
import datetime
import enum
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
    def trap(self, height: list[int]) -> int:

        # The trick with this question is to understand
        # that the amount of water that can be trapped at height[i]
        # is min(max height to the left, max height to the right) - height[i]

        # The above makes sense, but it's tricky to spot

        # After you know the above, you need to find the max height to
        # the left and right for each index. This can be done with two pre-computed
        # arrays.

        # Note that there is a solution that uses O(1) memory
        # with two pointers, but that's pretty unintuitive and would
        # likely not be your solution in an interview, so I'm just
        # doing the one with O(n) space complexity

        if len(height) < 3:
            return 0

        maxL = []
        maxR = [0] * len(height)

        ans = 0

        for i in range(len(height)):
            # This could be tidier with fewer ternaries, but it's fine for now
            curr = maxL[-1] if maxL else 0
            h = height[i - 1] if i > 0 else 0
            maxL.append(max(h, curr))

        for i in range(len(height) - 1, -1, -1):
            curr = maxR[i + 1] if i < len(height) - 1 else 0
            h = height[i + 1] if i < len(height) - 1 else 0
            maxR[i] = max(h, curr)

        for i, h in enumerate(height):
            res = min(maxL[i], maxR[i]) - h
            if res > 0:
                ans += res

        return ans


# @leet end
