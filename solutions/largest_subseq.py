#!/bin/python
def get_largest_sum_subseq(arr):
  max_latest = 0
  max_sum = 0
  for num in arr:
    max_latest = max([0, max_latest + num])
    max_sum = max([max_sum, max_latest])
  return max_sum
if __name__ == '__main__':
  arr = [1,2,3,-5, -8, -10, 10, 20, 30, -2, 10]
  print get_largest_sum_subseq(arr)
