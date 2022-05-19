"""Given a sorted number array and two integers 'K' and 'X', find 'K' closest numbers to 'X' in the array. 
Return the numbers in the sorted order. 
'X' is not necessarily present in the array."""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from concepts.search_algos import get_closest_value

from heapq import heapify

def find_closest_numbers(arr, K, X):
    result = []
  
    if len(arr) == 0: return result

    val, indx = get_closest_value(arr, X)
    # search for the closest k vals only in the vicinity of indx
    if len(arr) - indx > K:
        right_index = indx + K
    else:
        right_index = len(arr)

    if indx > K:
        left_index = indx - K
    else:
        left_index = 0
   

    diffs = [(abs(nr - X), nr) for nr in arr[left_index:right_index]]
    heapify(diffs)
    result = [el[1] for el in diffs[:K]]
    result.sort()

    return  result

def main():
    # Test case 1
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    res = find_closest_numbers(arr, k, x)
    print(res)
    assert res == [1,2,3,4]
     
    # Test case 2 
    arr = [2, 4, 5, 6, 9]
    k = 3
    x = 6
    
    res = find_closest_numbers(arr, k, x)
    print(res)
    assert res == [4, 5, 6]

if __name__ == "__main__":
    main()