

def binarySearch(low, hi, v, A):
  if hi - low == 1: ans = A[low] == v
  else:
    mid = (hi + low) // 2 # low + (hi - low) // 2
    if v < A[mid]: ans = binarySearch(low, mid, v, A)
    else: ans = binarySearch(mid, hi, v, A)
  return ans

def binarySearchIter(A, v):
  low, hi = 0, len(A)
  while hi - low > 1:
    mid = (hi + low) // 2
    if v < A[mid]: hi = mid
    else: low = mid
  ans = A[low] == v
  return ans

eps = 1e-6

def bisection(f, v, a, b):
  low, hi  = a, b
  while abs(hi - how) > eps:
    mid = (hi + low) / 2
    if v <= f(mid): hi = mid
    else: low = mid
  ans = low
  return ans
      
