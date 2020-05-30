def merge (a, b):
  n = len (a)
  m = len (b)
  i = 0
  j = 0
  ans = list ()
  while (i < n and j < m):
    if (a[i] < b[j]):
      ans.append (a[i])
      i += 1
    else:
      ans.append (b[j])
      j += 1
  while (i < n):
    ans.append (a[i])
    i += 1
  while (j < m):
    ans.append (b[j])
    j += 1
  return ans

def mergeSort (a):
  if (len (a) <= 1) :
    return a
  m = (len (a) - 1) // 2
  x = list ()
  y = list ()
  for i in range (m + 1):
    x.append (a[i])
  for i in range (m + 1, len (a)):
    y.append (a[i])
  x = mergeSort (x)
  y = mergeSort (y)
  return merge (x, y)

n = int (input ())
a = list (map (int, input ().split ()))
print (*a)
a = mergeSort (a)
print (*a)
