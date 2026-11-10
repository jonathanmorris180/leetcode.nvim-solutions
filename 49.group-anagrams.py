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
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list)

        for s in strs:
            hash = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                hash[idx] = hash[idx] + 1

            res[tuple(hash)].append(s)

        return list(res.values())


# @leet end
