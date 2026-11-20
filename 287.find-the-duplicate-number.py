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
    def findDuplicate(self, nums: list[int]) -> int:
        # This can be solved by treating `nums` as a linked list
        # where the value of nums[i] is a pointer to the next node.
        # We can then find the duplicate by using the tortoise and hare
        # algorithm in O(1) space.

        # Note: it's really important to start the algorithm off with the slow and
        # fast pointers on the first index, otherwise we can't detect the start
        # of the cycle

        # Initialize the pointers to the first iteration of slow and fast so they aren't
        # the same and the while loops can run
        s, f = nums[0], nums[nums[0]]

        while s != f:
            s, f = nums[s], nums[nums[f]]

        # Now find the start, which is the duplicate
        s = 0
        while s != f:
            s, f = nums[s], nums[f]

        return f


# @leet end
