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
class Node:
    def __init__(
        self,
        key: int = 0,
        val: int = 0,
        next: Node | None = None,
        prev: Node | None = None,
    ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    # This should be doable with a doubly-linked list
    # where the head of the list is the LRU key and the tail of the list
    # is the MRU key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def addToTail(self, newTail: Node) -> None:
        prev = self.tail.prev
        newTail.next, newTail.prev = self.tail, prev
        prev.next = newTail
        self.tail.prev = newTail

    def unlinkNode(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        cacheNode = self.cache.get(key, None)
        if not cacheNode:
            return -1
        # Move the node to the tail
        self.unlinkNode(cacheNode)
        self.addToTail(cacheNode)
        return cacheNode.val

    def printList(self):
        curr = self.head
        while curr:
            print(f"node key: {curr.key} val: {curr.val}")
            curr = curr.next

        print(f"size: {self.size}, cache: {self.cache}")
        print("===========")

    def put(self, key: int, value: int) -> None:
        cacheNode = self.cache.get(key, None)
        if cacheNode:
            # Unlink the node, move to tail
            cacheNode.val = value
            self.unlinkNode(cacheNode)
            self.addToTail(cacheNode)
            return
        if self.size == self.capacity:
            # Evict the LRU from the list and cache
            lru = self.head.next
            self.unlinkNode(lru)
            del self.cache[lru.key]
            self.size -= 1
        # Add to the tail
        self.addToTail(Node(key, value))
        self.cache[key] = self.tail.prev
        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end
