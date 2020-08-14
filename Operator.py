import math
import numpy as np
from State import *
from ComplexNum import *

class Operator(object):
  def __init__ (self, array):
    x = list(array.shape)
    if(len(x)==2 and x[0]>1 and x[1]==x[0]):
      self.array = array
    else:
      return None

  def __repr__(self):
    return str(self.array)
    
  def __mul__(self, other):
    if isinstance(other, State):
      return State.to_dict(np.matmul(self.array, other.to_array()))
    if isinstance(other, Operator):
      return Operator(np.matmul(self.array,other.array)) 
    return Operator(other*self.array)

  def __rmul__(self, other):
    return Operator(other*self.array)

  def __add__(self, other):
    return Operator(self.array + other.array)
  
  def __sub__(self, other):
    return Operator(self.array - other.array)

  def tensor(self, other):
    return Operator(np.kron(self.array, other.array))
  
  def __eq__(self, other):
    return np.all(self.array == other.array)

  def ComplexConjT(self):
    temp = np.array(self.array.transpose())
    for i in range(list(temp.shape)[0]):
      for j in range(list(temp.shape)[1]):
        if type(temp[i,j]) == ComplexNum:
          temp[i,j] = temp[i,j].conj()
    return Operator(temp)
  
  def isHermitian(self):
    return np.all(self.array == self.ComplexConjT().array)

  def eigenvalues(self):
    return np.linalg.eig(self.array)[0]

  def eigenvectors(self):
    return np.linalg.eig(self.array)[1]

  
class Sigma(Operator):
  def __init__(self, i):
    x = np.array([[0,1],[1,0]])
    y = np.array([[0, ComplexNum(0,-1)], [ComplexNum(0,1),0]])
    z = np.array([[1,0],[0,-1]])
    if i == 1:
      super().__init__(x)
    if i == 2:
      super().__init__(y)
    if i == 3:
      super().__init__(z)

class Hadamard(Operator):
  def __init__(self):
    H =(1/math.sqrt(2))*np.array([[1,1],[1,-1]])
    super().__init__(H)   
        
class Projection(Operator):
  def __init__(self, st, notation): 
    self.notation = notation  
    self.state = st
    super().__init__(st.to_array()*st.to_array().T)

  def __repr__(self):
    return "|{}〉〈{}|".format(self.notation, self.notation)

  def __mul__(self, other):  
    if isinstance(other, State):
      return (self.state*other)*self.state
    if isinstance(other, Operator):
      return Operator(np.matmul(self.array, other.array)) 
    return Operator(other*self.array)
    
  
class CNOT(Operator):
  def __init__(self):
    c = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    super().__init__(c)

class CZ(Operator):
  def __init__(self):
    c = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])
    super().__init__(c)

class CY(Operator):
  def __init__(self):
    c = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,ComplexNum(0,-1)],[0,0,ComplexNum(0,1),0]])
    super().__init__(c) 

class Toffoli(Operator):
  def __init__(self):
    t = np.zeros((8,8))
    for i in range(6):
      t[i,i]=1
    t[7,6]=1
    t[6,7]=1
    super().__init__(t)

class SWAP(Operator):
  def __init__(self):
    s = c = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    super().__init__(s)

class Identity(Operator):
  def __init__(self, n):
    super().__init__(np.identity(2**n))
  
class Phase(Operator):
  def __init__(self):
    super().__init__(np.array([[1,0],[0,ComplexNum(0,1)]]))

class Pi8(Operator):
  def __init__(self):
    super().__init__(np.array([[1,0],[0, ComplexNum(1/math.sqrt(2),1/math.sqrt(2))]]))
