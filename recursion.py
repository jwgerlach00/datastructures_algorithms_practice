from typing import List


def count_up(max_num:int) -> List[int]:
    '''Return a list of numbers from 1 to max_num, inclusive.'''
    if max_num == 1: # base case --> simplist case, stops from looping forever
        return [1]
    return count_up(max_num - 1) + [max_num]

def factorial(n:int) -> int:
    '''n*...*4*3*2*1'''
    if n == 1: # base case --> simplist case, stops from looping forever
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    # count_up
    assert count_up(10) == list(range(1, 10+1))
    
    # factorial
    assert factorial(5) == 5*4*3*2*1
