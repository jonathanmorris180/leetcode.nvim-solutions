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
    def maxArea(self, height: list[int]) -> int:
        # The standard solution for this is a two-pointer solution
        # where you start with pointers on both ends and move inward
        # based on which pointer is smaller in the hopes of finding a larger
        # bar (i.e., if l = 1 and r = 6, move l inward in the hopes of finding something > 1)

        # The two-pointer solution is pretty easy

        # There is also a more complicated solution
        # Where you sort the bars by height:

        # The sorting solution is the one I initially came up with
        # but I had to get AI assistance to see it through to the end.
        # The missing piece of understanding was that since each bar you
        # iterate over in the sorted array is at least as tall as the previous
        # bar (i.e., the height of bars[i] >= bars[i - 1]), the only thing you care about
        # to compute the max container that bar can be part of is the
        # minimum and maximum index of all the bars you have visited so far

        # Adding the sorting solution here:

        ###########

        # Pair each bar's index with its height, then sort by height descending.
        # enumerate(height) yields (index, height) pairs, so p[1] is the height.
        # After sorting, the tallest bars come first.
        bars = sorted(enumerate(height), key=lambda p: -p[1])

        # lo and hi track the smallest and largest index among bars already visited.
        # Start with the tallest bar's index. It has no partner yet, so both are the same.
        lo = hi = bars[0][0]

        # Best (largest) area found so far.
        best = 0

        # Skip the first bar since it's already used to initialize lo and hi.
        for i, h in bars[1:]:
            # Every visited bar is at least as tall as this one, so this bar's
            # height h is the limiting height for any pair it forms with them.
            #
            # The widest container comes from the visited index farthest from i.
            # The farthest index in a set is always one of its extremes, so we
            # only need to compare the distance to lo and the distance to hi.
            width = max(abs(i - lo), abs(i - hi))

            # Area = limiting height * width. Keep it if it beats the best so far.
            best = max(best, h * width)

            # Mark this bar as visited by widening the min/max index range.
            # Later (shorter) bars will consider this bar as a possible partner.
            lo, hi = min(lo, i), max(hi, i)

        return best


# @leet end
