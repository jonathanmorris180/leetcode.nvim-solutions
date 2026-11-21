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
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We can do this by tracking the seen
        # characters in a set and using two pointers
        # to track the contiguous chars

        if len(s) <= 1:
            return len(s)

        maxSize = 0
        seen = {s[0]}

        l, r = 0, 1

        while r < len(s):
            if s[r] in seen:
                maxSize = max(maxSize, len(seen))
                seen = set()
                while r + 1 > len(s) and s[r + 1] == s[r]:
                    r += 1
                seen.add(s[r])
                l = r
                while l - 1 > 0 and s[l - 1] != s[l] and s[l - 1] not in seen:
                    l -= 1
                    seen.add(s[l])
                r += 1
                continue
            seen.add(s[r])
            maxSize = max(maxSize, len(seen))
            r += 1

        return maxSize


# @leet end
