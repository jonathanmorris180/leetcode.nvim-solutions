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
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        pending = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # Create a monotonically decreasing stack
            # (i.e., we always pop elements from the top of the stack if they are less than the current one)
            while pending and pending[-1][1] < temp:
                idx = pending.pop()[0]
                ans[idx] = i - idx
            pending.append((i, temp))

        return ans


# @leet end
