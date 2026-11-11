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
    def evalRPN(self, tokens: list[str]) -> int:

        # You just need a single stack for this since you can push each result
        # back onto the stack after it's been computed
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(token)
            elif token == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second) + int(first))
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second) - int(first))
            elif token == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second) * int(first))
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                # Truncate towards zero with int() or math.trunc()
                stack.append(int(int(second) / int(first)))

        return int(stack[0])


# @leet end
