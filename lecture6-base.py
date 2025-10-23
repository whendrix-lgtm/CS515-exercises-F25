import random

'''
  Standard shuffling function
  Shuffles input list so that all permutations are equally likely
'''
def shuffle(data):
  for i in range(len(data)-1, 0, -1):
    r = random.randint(0, i)
    data[r], data[i] = data[i], data[r]

'''
  Binary search
  Returns the index of target in sorted list data
  Returns -1 if not present
  Undefined behavior if unsorted
'''
def binsearch(data, t):
  lo = 0
  hi = len(data)
  while lo < hi - 1:
    mid = (lo + hi) // 2
    if data[mid] == t:
      return mid
    elif t < data[mid]:
      hi = mid
    else:
      lo = mid+1
  if lo >= len(data) or data[lo] != t:
    return -1
  else:
    return data[lo]

'''
  Implements SelectionSort
  Iteratively swaps the min to the next position
'''
def selectionsort(data):
  # For i = 0 to n-1:
    # min = index of min(data[i..n])
    # Swap data[i] and data[m]
  return data

'''
  Implements InsertionSort
  Iteratively inserts next element into sorted list to its left
'''
def insertionsort(data):
  # For i = 1 to n-1:
    # Shift all values > data[i] right, starting with data[i-1]
    # Stop at j == 0 or data[j-1] >= ins
  return data

'''
  Implements MergeSort
  Recursively sort left and right halves and merge them
'''
def mergesort(data):
  # Base case:  n <= 1 (no change)
  # mid = floor(n / 2)
  # mergesort both halves

  # while left and right sides are not empty:
    # if next(left) < next(right)
      # add next(left) to data
    # otherwise,
      # add next(right) to data
  # copy remainder of left and right to data
  return data

'''
  Implements QuickSort
  Chooses a random pivot, partitions list, and recursively sorts each side
  start:  first index of current subarray (default 0)
  end:  index just past end of current subarray (default len(data))
'''
def quicksort(data, start = None, end = None):
  if start == None:
    start = 0
  if end == None:
    end = len(data)
  # Base case:  n <= 1 (do nothing)
  # Choose random pivot and swap to data[start]

  # Start at left and right ends of subarray
    # Increment left while left < right and value <= pivot
    # Decrement right while left < right and value >= pivot
    # Swap elements at left and right

  # Move left pointer backwards if value > pivot
  # Swap pivot to left pointer

  # Recurse on both sides
  return data

'''
  Test function for binsearch
  Searches for elements in all positions
  Checks for missing elements at start, middle, and end of list
'''
def test_binsearch():
  errors = 0
  test = [i for i in range(100)]
  for i in range(100):
    if binsearch(test, i) != i:
      errors += 1
  if errors:
    print(f"BinSearch could not locate {errors} / 100 elements")
  test.remove(48)
  if binsearch(test, -12) != -1:
    print('BinSearch did not return -1 correctly at the beginning')
  if binsearch(test, 48) != -1:
    print('BinSearch did not return -1 correctly in the middle')
  if binsearch(test, 256) != -1:
    print('BinSearch did not return -1 correctly at the end')

'''
  Attempts to evaluate the shuffle function
  Shuffles the array 1-10 ten times and prints result
'''
def test_shuffle():
  test = [i+1 for i in range(10)]
  print('Shuffled lists:')
  for i in range(10):
    print(shuffle(test[:]))

'''
  Test suite for given sorting function
  Assumes function accepts and returns a list
  Sorts 100 shuffled lists
  Prints failure rate and last output if unsuccessful
  Prints nothing if correct
'''
def test_sort(sort_fn):
  errors = 0
  test = [i for i in range(100)]
  for i in range(100):
    data = test[:]
    shuffle(data)
    data = sort_fn(data)
    if data != test:
      errors += 1
  if errors:
    print(f'{sort_fn.__name__} failed to sort {errors} / 100 times')
    print(f'Sample output:  {data}')

if __name__ == '__main__':
  test_binsearch()
  #test_shuffle()
  #test_sort(selectionsort)
  #test_sort(insertionsort)
  #test_sort(mergesort)
  #test_sort(quicksort)
