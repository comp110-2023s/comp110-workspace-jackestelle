"""EEX04 - `list` Utility Functions."""

__author__ = "730558551"


def all(lst: list[int], num: int) -> bool:
    """Checks if all items in lst are equal to num."""
    i: int = 0
    if len(lst) == 0:
        return False
    
    while (i < len(lst)):
        if (lst[i] != num):
            return False
        i += 1
    return True


def max(int_lst: list[int]) -> int:
    """Determines maximum value in lst."""
    if len(int_lst) == 0:  # empty list -> ValueError
        raise ValueError("List cannot be empty")
    
    max_num: int = (int_lst[0])
    ind: int = 0

    while (ind < len(int_lst)):
        if (int_lst[ind] > max_num):  
            max_num = int_lst[ind]
        ind += 1
    return max_num


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Determines if lst1 and lst2 are equal."""
    if lst1 == lst2:
        return True
    else:
        return False
        
