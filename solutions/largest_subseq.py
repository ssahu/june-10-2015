#!/bin/python
def get_largest_sum_subseq(arr):
  max_latest = arr[0]
  max_sum = max_latest
  for num in arr[1:]:
    max_latest = max([num, max_latest + num])
    max_sum = max([max_sum, max_latest])
  return max_sum
if __name__ == '__main__':
  arr = [1,2,3,-5, -8, -10, 10, 20, 30, -2, 10]
  print get_largest_sum_subseq(arr)
