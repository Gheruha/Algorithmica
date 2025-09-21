# Problem 2 - Add two numbers.
# Medium
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
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        num3 = str(int(num1) + int(num2))
        dummy = ListNode()
        current = dummy
        for char in num3[::-1]:
            current.next = ListNode(int(char))
            current = current.next

        return dummy.next


# @leet end
