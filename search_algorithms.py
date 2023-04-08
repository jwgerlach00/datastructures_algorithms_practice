from typing import Any, List
from bisect import bisect_left


def linear_search(li:list, target:Any) -> bool:
    '''O(n) to determine if target is in li.'''
    for el in li:
        if el == target:
            return True
    return False

def binary_search(sorted_li:list, target:Any) -> bool:
    '''
    O(log n) to determine if target is in sorted_li. MUST BE SORTED!
    
    log n is inverse of exponential:
      - step 1: n/2 items left
      - step 2: n/2/2 items left
      - step 3: n/2/2/2 items left
      (...)
      - step x: n/2^x items left
    
    equation for how many steps to realize number not present:
        2**n = len(sorted_li) --> solve for n --> log_2(len(sorted_li))
    '''
    if sorted_li == []:
        return False
    
    mid = len(sorted_li) // 2
    
    if sorted_li[mid] == target:
        return True
    if sorted_li[mid] > target:
        return binary_search(sorted_li[:mid], target)
    elif sorted_li[mid] < target:
        return binary_search(sorted_li[mid+1:], target)
    
def binary_search_w_bisect(sorted_li:list, target:Any) -> bool:
    '''Binary search using bisect module.'''
    bisect_i = bisect_left(sorted_li, target)
    if target == sorted_li[bisect_i] and bisect_i < len(sorted_li): # could return greater than len(sorted_li) if target 
        # is greater than all elements in sorted_li
        return True
    return False

def book_bin_search(a_list:list, n:Any):
    '''Binary search from the book.'''
    first = 0
    last = len(a_list) - 1 # negative 1 when empty list
    while last >= first: # while there are still elements to search
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        elif a_list[mid] < n:
            first = mid + 1
        else:
            last = mid - 1

def char_binary_search(sorted_li:List[str], target:str) -> bool:
    '''Binary search for characters.'''
    if sorted_li == []:
        return False
    
    mid = len(sorted_li) // 2
    
    targ_val = ord(target)
    el_val = ord(sorted_li[mid])
    
    if el_val == targ_val:
        return True
    if el_val > targ_val:
        return binary_search(sorted_li[:mid], target)
    elif el_val < targ_val:
        return binary_search(sorted_li[mid+1:], target)


if __name__ == '__main__':
    # linear_search
    assert linear_search([1, 2, 3, 4, 5], 3) == True
    assert linear_search([1, 2, 3, 4, 5], 6) == False
    
    # binary_search
    assert binary_search([1, 2, 3, 4, 5], 3) == True
    assert binary_search([1, 2, 3, 4, 5], 6) == False
    
    # binary_search_w_bisect
    assert binary_search([1, 2, 3, 4, 5], 3) == True
    assert binary_search([1, 2, 3, 4, 5], 6) == False
    
    # char_binary_search
    assert char_binary_search(['a', 'b', 'c', 'd', 'e'], 'c') == True
    assert char_binary_search(['a', 'b', 'c', 'd', 'e'], 'f') == False

    # word_binary_search
    assert binary_search(['apple', 'banana', 'cherry', 'date', 'eggplant'], 'apple') == True
    assert binary_search(['apple', 'banana', 'cherry', 'date', 'apple2', 'eggplant'], 'apple2') == False # Not sorted
