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
    def characterReplacement(self, s: str, k: int) -> int:
        # Potential solution:
        # Keep track of the count of the most frequent character
        # using an l and r pointer and a hashmap. When
        # (length of window) - (char with largest count in window) > k,
        # move the l pointer up, decreasing the counts appropriately.
        # Keep track of the max(len(window))

        l, r = 0, 0
        counts = defaultdict(int)
        res = 0

        while r < len(s):
            counts[s[r]] += 1
            # This can be optimized even further to remove
            # the max() scan below since the window doesn't
            # actually ever to shrink if you've already found
            # a valid window with greater size.
            while r - l + 1 - max(counts.values()) > k:
                # This can never go below 0 since
                # we're only removing what we added
                counts[s[l]] = counts[s[l]] - 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res


# @leet end
