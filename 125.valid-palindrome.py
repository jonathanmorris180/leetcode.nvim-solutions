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
    def isPalindrome(self, s: str) -> bool:
        # Could do this recursively or with two pointers
        # If it doesn't have an even number of characters, it's not a palindrome
        # First, construct the string without special chars
        filteredS = "".join([st for st in s if st.isalnum()])

        if not filteredS:
            return True

        l, r = 0, len(filteredS) - 1
        while l <= r:
            if filteredS[l].lower() != filteredS[r].lower():
                return False
            l += 1
            r -= 1

        return True


# @leet end
