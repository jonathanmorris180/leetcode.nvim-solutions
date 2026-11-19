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
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        # This can probably be done with a hashmap
        # where you iterate through the original list and check if the
        # hashmap has the `random` node

        # The hashmap will store the original node as the key and the
        # cloned version of the node as the value

        # If the map doesn't have the cloned value, we create one

        # Note: The code could probably be simplified by doing
        # two passes rather than one, but this is actually more efficient

        cloned = {}
        prev = None
        newHead = None

        while head:
            new = cloned.get(head, Node(head.val))
            cloned[head] = new
            if not newHead:
                newHead = new
            if head.random and not cloned.get(head.random, None):
                cloned[head.random] = Node(head.random.val)
            new.random = cloned.get(head.random, None)
            if prev:
                prev.next = new
            prev = new
            head = head.next

        return newHead


# @leet end
