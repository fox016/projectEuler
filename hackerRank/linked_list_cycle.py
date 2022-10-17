#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None:
        return 0
    visited_set = set()
    cur_node = head
    while cur_node != None:
        node_id = id(cur_node)
        if node_id in visited_set:
            return 1
        visited_set.add(node_id)
        cur_node = cur_node.next
    return 0

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        print(str(int(result)) + '\n')
