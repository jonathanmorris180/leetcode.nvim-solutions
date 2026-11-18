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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        # To do this with O(1) space and in O(n) time,
        # we can use two pointers and move one of them through
        # to node n and then move both of them through to
        # the end of the list. When the node that is ahead
        # reaches the end of the list, the first node will be n nodes away
        # from the end.

        # First, initialize two pointers
        dummy = ListNode(0, head)
        first, second = dummy, head

        # Move the second pointer
        i = 0
        while i < n:
            second = second.next
            i += 1

        # Find the end
        while second:
            second = second.next
            first = first.next

        # Remove the node
        first.next = first.next.next
        return dummy.next


# @leet end
