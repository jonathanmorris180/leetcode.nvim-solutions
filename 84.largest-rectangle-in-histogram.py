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
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Use a stack to track the start index and the height
        # where each rectangle can be made

        # Critical rule: A rectangle can only be extended to the right if
        # the subsequent bar is higher than the current one

        stack = []
        maxH = 0

        for i, h in enumerate(heights):
            if not stack or stack[-1][1] < h:
                stack.append((i, h))
            elif stack[-1][1] > h:
                start = 0
                while stack and stack[-1][1] > h:
                    # We need to calculate the max
                    # and pop from the stack
                    start, height = stack[-1]
                    width = i - start
                    area = width * height
                    maxH = max(maxH, area)
                    stack.pop()
                stack.append((start, h))

        while stack:
            start, height = stack[-1]
            width = len(heights) - start
            area = width * height
            maxH = max(maxH, area)
            stack.pop()
        return maxH


# @leet end
