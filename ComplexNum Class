class ComplexNum():
  def __init__(self, re, im):
    self.re = re
    self.im = im

  def __repr__(self):
    if self.im==0:
      return "{}".format(self.re)
    if self.re == 0:
      if self.im ==1 :
        return "i"
      if self.im ==-1:
        return "-i"
      return "{}".format(self.im)
    if self.im==0:
      return self.re
    if self.im ==1:
      return "{} + i".format(self.re)
    if self.im == -1:
      return "{} - i".format(self.re)
    if self.im <0:
      return "{} - {}i".format(self.re, -self.im)     
    return "{} + {} i".format(self.re, self.im)

  
  def __eq__(self, other): 
    if isinstance(other, ComplexNum):
      return self.re == other.re and self.im == other.im
    return False
  
  def __add__(self, other): 
    if isinstance(other, ComplexNum):
      return ComplexNum(self.re+other.re, self.im + other.im)
    return ComplexNum(other + self.re, self.im)
  
  def __sub__(self, other):
    if isinstance(other, ComplexNum):
      return ComplexNum(self.re-other.re, self.im - other.im)
    return ComplexNum(self.re - other, self.im)

  def __mul__(self, other):
    if isinstance(other, ComplexNum):
      return ComplexNum(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im )
    return ComplexNum(self.re*other, self.im*other)

  def __radd__(self, other): 
    if isinstance(other, ComplexNum):
      return ComplexNum(self.re+other.re, self.im + other.im)
    return ComplexNum(other + self.re, self.im)
  
  def __rsub__(self, other):
    if isinstance(other, ComplexNum):
      return ComplexNum(other.re - self.re, other.im - self.im)
    return ComplexNum(other - self.re, self.im)

  def __rmul__(self, other):
    if isinstance(other, ComplexNum):
      return ComplexNum(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im )
    return ComplexNum(self.re*other, self.im*other)


  def conj(self):
    return ComplexNum(self.re, -self.im)
