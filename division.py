# algorithm to divide the number which runs in O(log(x)) 
def division(x, y):
  x, y = abs(x), y = abs(y)
  start = 0
  end = x
  while end - start > 1:
    mid = start + (end - start) // 2
    mul = y * mid
    if mul > x:
      end = mid
    elif mul < x:
      start = mid
    else:
      return mid
  returns start
