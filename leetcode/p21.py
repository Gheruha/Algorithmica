# EASY
# Problem 21: Merge two sorted Linked Lists.
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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        bucket = []
        while list1:
            bucket.append(list1.val)
            list1 = list1.next

        while list2:
            bucket.append(list2.val)
            list2 = list2.next

        if len(bucket) != 0:
            bucket.sort()
            merged = ListNode(bucket[0])
            dummy = merged

            for i in range(1, len(bucket)):
                merged.next = ListNode(bucket[i])
                merged = merged.next

            return dummy
        else:
            return None


# @leet end
