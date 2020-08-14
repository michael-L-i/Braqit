class State(object):
    def __init__(self, clist):
      if set(clist.values()) == {0} or clist == {}:
        self.clist = {}
      else:
        self.clist=clist
        delete = []
        for k in self.clist:
          if self.clist[k]==0:
            delete += [k]
        for el in delete:
          del self.clist[el]
          # number of qbits/spins
        self.n =  len(list(self.clist.keys())[0])
          # dimension of Hilbert space
        self.N = 2**self.n

    def __repr__(self):
       #return "State({})".format(self.clist)  #"State(%s)" % self.clist
       if self.clist=={}: 
         return "0"
       res = ""
   
       for key in self.clist.keys():
        if not type(self.clist[key])==ComplexNum: 
          if self.clist[key] > 0 and self.clist[key]!=1:
            if res == "":
              res = "{}|{}〉".format(self.clist[key],key)
            else:
              res += " + {}|{}〉".format(self.clist[key], key)
          elif self.clist[key] ==1:
            if res == "":
              res = "|{}〉".format(key)
            else:
              res += " + |{}〉".format(key)
          elif self.clist[key]<0 and self.clist[key] != -1:
              res += " – {}|{}〉".format(-self.clist[key], key)
          elif self.clist[key] == -1:  
            res += " – |{}〉".format(key)
          if self.clist[key]==0:
            delete += key
        else:
          if res == "":
            res += "({})|{}〉".format(self.clist[key], key)
          else: 
            res += " + ({})|{}〉".format(self.clist[key], key)
       return res 

    def __add__(self, other): 
        a = self.to_array()
        b = other.to_array()
        c = a+ b
        return State.to_dict(c) 

    def __rmul__(self, n): 
      return self*n

    def __mul__(self, n): 
      if isinstance(n, State):
        return np.dot(self.to_array().T, n.to_array())[0,0]
      a = self.clist
      c = {}
      for x in a:
        c[x] = a[x]*n
      return State(c)
    
    def __sub__(self, other):
      a = self.clist
      b = other.clist
      c = dict({})
      for x in a:
        c[x] = a[x]-b[x]
      return State(c)

    def tensor(self, other):
      return State.to_dict(np.kron(self.to_array(), other.to_array()))
    
    def __eq__(self, other):
      return np.all(self.to_array()==other.to_array())
      
    def normalize(self):
      c = 0
      for key in self.clist:
        if type(self.clist[key]) == ComplexNum:
          c += self.clist[key]*(self.clist[key].conj())
        else:
          c = c + (self.clist[key])**2
      if c == 0:
        self.clist = {}
      else:
        d = 1/(math.sqrt(c))
        self.clist = (self*d).clist    
   
    
    def get_prob(self, key): 
      self.normalize()
      if type(self.clist[key]) == ComplexNum:
        return self.clist[key]*(self.clist[key].conj())
      else:
        return self.clist[key]**2         

    def get_probabilities(self):
      res = np.zeros((self.N,1))  
      for i in range (self.N):
        if np.binary_repr(i, self.n) in self.clist:
          res[i,0] = self.get_prob(np.binary_repr(i, self.n))
      return res

    def to_array(self): 
        temp = np.zeros((self.N,1))
        for k in range(self.N):
          binarym = np.binary_repr(k, self.n)
          if binarym in self.clist:
            temp[k,0] = self.clist[binarym]       
        return temp

    @staticmethod
    def to_dict(arr):
      templist = {}
      for i in range(0, arr.shape[0]):
        if arr[i, 0]!=0:
          templist[np.binary_repr(i, int(math.log2(arr.shape[0])))] = arr[i, 0]
      return State(templist)

    def measure_second_register(self):
          x=self.clist.keys()
          k= random.choice(x)[-2]
          for key in x:
              if key[-2] != k:
                  del self.clist[key]

class PureState(State):
  def __init__(self):
    return 1

class UniformState(State):

  def __init__(self, n):
    D = {}
    for i in range (0, 2**n): 
      D[np.binary_repr(i, n)]  = 1
    super().__init__(D)
