class minheap(object):
  """implements minimal heaps of numbers"""

  def __init__(self):
    """create an empty minheap"""
    self.__A = list()

  def __len__(self):
    """return the number of elements in the collection"""
    return len(self.__A)

  def __str__(self):
    """return the string representation of the heap"""
    return str(self.__A)

  def __parent(self, i):
    """return the index of the parent of i in its array representation"""
    assert i!=0
    return (i-1)>>1

  def __left(self, i):
    """return the index of the left son of i in its array representation"""
    return (i<<1)+1
  
  def __right(self, i):
    """return the index of the right son of i in its array representation"""
    return (i+1)<<1

  def getMin(self):
    """return the minimum element of the collection if it exists;
    otherwise, an error is generated"""
    assert len(self)!=0
    return self.__A[0]

  def add(self, x):
    """add x to the collection maintaining the minheap property"""
    self.__A.append(x)
    self.__heapifyUp(len(self)-1)

  def __heapifyUp(self, i):
    """implement the heapifyup function"""
    if i!=0:
      ip = self.__parent(i)
      if self.__A[i]<self.__A[ip]:
        self.__A[i],self.__A[ip] = self.__A[ip],self.__A[i]
        self.__heapifyUp(ip)

  def removeMin(self):
    """remove the minimum of the collection if exists; otherwise, an
    error is generated"""
    assert len(self)!=0
    self.__A[0] = self.__A[-1]
    self.__A.pop()
    self.__heapifyDown(0)
    
  def __heapifyDown(self, i):
    """implement the heapifydonw function from index i"""
    N,ibest,il,ir = len(self),i,self.__left(i),self.__right(i)
    if il<N and self.__A[ibest]>self.__A[il]: ibest = il
    if ir<N and self.__A[ibest]>self.__A[ir]: ibest = ir
    if ibest!=i:
      self.__A[i],self.__A[ibest] = self.__A[ibest],self.__A[i]
      self.__heapifyDown(ibest)
  
