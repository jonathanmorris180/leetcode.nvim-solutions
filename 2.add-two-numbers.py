# @leet imports start
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
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:

        # This can be done by simply iterating through the lists
        # and adding the numbers one at a time

        # We will need to carry the remainder to the next iteration for each addition
        # and the construct the return value

        # We'll need to account for lists of different length

        rem = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2:
            newNode = ListNode()
            if l1 and l2:
                newVal, rem = self.calculateVals([l1.val, l2.val, rem])
                newNode.val = newVal
                l1 = l1.next
                l2 = l2.next
            elif not l2:
                newVal, rem = self.calculateVals([l1.val, rem])
                newNode.val = newVal
                l1 = l1.next
            else:
                newVal, rem = self.calculateVals([l2.val, rem])
                newNode.val = newVal
                l2 = l2.next
            curr.next = newNode
            curr = curr.next

        if rem:
            newNode = ListNode(rem)
            curr.next = newNode
            rem = 0

        return dummy.next

    def calculateVals(self, toAdd: list[int]):
        tmpRem = sum(toAdd) // 10
        newVal = sum(toAdd) % 10
        rem = max(0, tmpRem)
        return newVal, rem


# @leet end
