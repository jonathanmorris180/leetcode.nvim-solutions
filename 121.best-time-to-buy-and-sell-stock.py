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
    def maxProfit(self, prices: list[int]) -> int:
        # We need to evaluate each day as a potential
        # sell day by comparing the min value seen to
        # that point with the value at the current index

        if len(prices) < 2:
            return 0

        minBuy = 0
        largest = 0

        for i in range(1, len(prices)):
            minBuy = i if prices[i] < prices[minBuy] else minBuy
            largest = max(largest, prices[i] - prices[minBuy])

        return largest


# @leet end
