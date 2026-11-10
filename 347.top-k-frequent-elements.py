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
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Need to use a heap for this. Process:
        # 1. Calculate the frequency of each element
        # 2. Create a min heap where the values in the heap that are compared are the frequencies (can use a tuple)
        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            while len(heap) > k:
                # We do this so that only the elements with the highest counts
                # survive in the heap Otherwise, we would end up popping the
                # elements with the smallest frequencies first

                # Alternative would be to use a max heap
                # or multiply the counts by -1
                heapq.heappop(heap)

        i = 0
        while i < k:
            res.append(heapq.heappop(heap)[1])
            i += 1

        return res


# @leet end
