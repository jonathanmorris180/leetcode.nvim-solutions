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
    def missingNumber(self, nums: list[int]) -> int:
        exists = [False] * (len(nums) + 1)

        for num in nums:
            exists[num] = True

        for i, res in enumerate(exists):
            if not res:
                return i

        return 0


# @leet end
