def recursive_bubble_sort(li:list) -> list:
    '''
    My recursive implementation of bubble sort.
    O(n^2)
    '''
    def compare_swap(li:list, i:int) -> list:
        '''Inner function for swapping values.'''
        if i + 1 >= len(li): # avoid indexing out of range
            return li
        
        curr_i, next_i = li[i], li[i + 1]
        
        if curr_i <= next_i: # return if next element is greater
            return li
        
        li[i], li[i + 1] = next_i, curr_i
        return compare_swap(li, i + 1)
    
    if len(li) == 1: # down to the last element --> return
        return li
    
    li[-1] = compare_swap(li, 0)[-1]
    return recursive_bubble_sort(li[:-1]) + [li[-1]]

def iterative_bubble_sort(li:list) -> list:
    '''
    My implementation of iterative before seeing book.
    Two nested for loops --> O(n^2)
    '''
    for i in range(len(li)):
        for j in range(i + 1, i + len(li[i:])): # everything to the right of i
            if li[i] <= li[j]:
                break
            li[i], li[j] = li[j], li[i]
    return li

def book_bubble_sort(li:list) -> list:
    '''
    Algorithm taken straight from the book.
    Two nested for loops --> O(n^2)
    '''
    list_length = len(li) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i): # subtract i because don't need to compare with what already "bubbled up"
            # largest number is at end after first iteration, then 2nd largest is 2nd last after 2nd iteration, etc.
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                no_swaps = False
        if no_swaps: # adding this makes algorithm significantly faster when the list is nearly sorted
            return li
    return li

def char_iterative_bubble_sort(li:list) -> list:
    '''My implementation of iterative before seeing book.'''
    for i in range(len(li)):
        for j in range(i + 1, i + len(li[i:])): # everything to the right of i
            if ord(li[i]) <= ord(li[j]):
                break
            li[i], li[j] = li[j], li[i]
    return li


if __name__ == '__main__':
    '''
    Bubble sort
        - O(n^2)
            - two nested for loops
            - worst case, n passes of li and swap adjacent elements so n^2 comparisions
        - stable
            - elements with the same value will remain in original order:
                ex: sorting by first char: [apple, banana, ape] --> [apple, ape, banana] ALWAYS
    '''
    
    # Bubble sort
    assert all([func([5, 4, 2, 1, 3]) == list(range(1, 5 + 1)) for func in 
                [recursive_bubble_sort, iterative_bubble_sort, book_bubble_sort]])
    
    # char_iterative_bubble_sort
    assert char_iterative_bubble_sort(['a', 'c', 'b', 'f', 'd']) == ['a', 'b', 'c', 'd', 'f']
