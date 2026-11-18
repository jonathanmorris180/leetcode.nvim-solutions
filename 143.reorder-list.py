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
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # The easiest way to solve this is to create a reversed
        # version of the list and then create the final list

        # In my original approach, I was going to create a new version
        # of the list in memory by walking the whole list and creating
        # a new ListNode, but that creates a problem in finding
        # the middle of both lists

        # The better way to do this is actually to use a fast and
        # slow pointer to find the middle of the list and then reverse
        # just one half of the list

        # Note: The slow pointer needs to be at node 0 and the fast one
        # needs to be at node 1 in order for this to work correctly
        # or else you get off by one errors

        if not head or not head.next:
            return head

        # First find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev now points to the start of the second half

        # Now merge the lists
        while head and prev:
            tmpHead = head.next
            tmpPrev = prev.next
            head.next = prev
            prev.next = tmpHead
            head = tmpHead
            prev = tmpPrev


# @leet end
