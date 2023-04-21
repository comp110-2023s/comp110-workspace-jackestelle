"""EEX04 - `list` Utility Functions"""
__author__ = "730558551"

def all(lst, num) -> bool:
    """Checks if all items in lst are equal to num"""
    if not lst:  
        return False
    n == 0
    while n < len(lst):
        if lst[n] != num:
            return False
        n += 1
    return True 

def max(lst) -> int:
    """Determines maximum value in lst"""
    if len(input) == 0:  #empty list -> ValueError
        raise ValueError("List cannot be empty")
    max_num = lst[0] 
    n == 0
    while n < len(lst):
        if lst[n] > max_num:  
            max_num = lst[n]
        n +=1
    return max_num

def is_equal(lst1, lst2):
    """Determines if lst1 and lst2 are equal"""
    if len(lst1) != len(lst2):  
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True 
