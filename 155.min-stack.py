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
class MinStack:

    def __init__(self):
        self.min = []
        self.order = []

    def push(self, value: int) -> None:
        self.order.append(value)
        # >= because we need to track if the same minimum has been added more than once
        if not self.min or self.min[-1] >= value:
            self.min.append(value)

    def pop(self) -> None:
        curr = self.order.pop()
        if self.getMin() == curr:
            self.min.pop()

    def top(self) -> int | None:
        return self.order[-1] if self.order else None

    def getMin(self) -> int | None:
        return self.min[-1] if self.min else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
