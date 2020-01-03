'''
The Deaf Rats of Hamelin
https://www.codewars.com/kata/the-deaf-rats-of-hamelin/train/python

Story
The Pied Piper has been enlisted to play his magical tune and coax all 
the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
'''

def count_deaf_rats(town):
    # Your code here
    t = town.replace(' ', '')
    p_index = t.index('P')
    left = t[:p_index][::2].count('O')
    right = t[p_index+1:][::2].count('~')
    return left + right