# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
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
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        curr_result = result
        rem = 0

        while l1 or l2:
            val = 0
            local_rem = 0
            if l1 and l2:
                sum = l1.val + l2.val
                val = sum % 10
                local_rem = sum // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            elif l2:
                val = l2.val
                l2 = l2.next
            sum = val + rem
            if sum >= 10:
                val = sum % 10
                local_rem = sum // 10
            else:
                val = sum
            curr_result.next = ListNode(val)
            curr_result = curr_result.next
            rem = local_rem

        if rem > 0:
            curr_result.next = ListNode(rem)

        return result.next


# @leet end
