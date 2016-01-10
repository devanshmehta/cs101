# algorithm to divide the number which runs in O(log(x)) 
def division(x, y):
  if y == 0:
    raise ValueError(str(y) + " divisor passed")
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
  
def slow_division(x, y):
  if y == 0:
    raise ValueError(str(y) + " divisor passed")
  x, y = abs(x), abs(y)
  count = 0
  while x > y:
    x -= y
    count += 1
  return count
