from math import factorial

def pascal_tri(numRows):
  '''Print Pascal's triangle with numRows.'''
  for i in range(numRows):
    print(' '*(numRows-i), end='')
    # compute power of 11
    print(' '.join(str(11**i)))

pascal_tri(5)