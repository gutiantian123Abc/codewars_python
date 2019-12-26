'''
Can you get the loop 

https://www.codewars.com/kata/can-you-get-the-loop/train/python

You are given a node that is the beginning of a linked list.
 This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.
'''

def loop_size(node):
    p1, p2 = node, node.next
    
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next.next  
        
    c = 1
    p2 = p2.next
    while p1 != p2:
        p2 = p2.next
        c += 1
        
    return c