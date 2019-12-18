'''
Your task is to make a function that can take any non-negative 
integer as a argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1234
'''
def descending_order(num):
    # Bust a move right here
    return int("".join(sorted(str(num), reverse=True)))