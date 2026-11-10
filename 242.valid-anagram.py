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
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = [0] * 26
        countT = [0] * 26

        # Could do this with a single iteration actually
        # since both strings are the same length,
        # but this was my initial solution

        for char in s:
            idx = ord(char) - ord("a")
            countS[idx] += 1

        for char in t:
            idx = ord(char) - ord("a")
            countT[idx] += 1

        for i in range(len(countT)):
            if countS[i] != countT[i]:
                return False

        return True


# @leet end
