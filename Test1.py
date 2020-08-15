from Operator import *
from State import *
from ComplexNum import *
from Algorithm import *


# Creating the state |00⟩ + |11⟩
st = State({"00":1, "11":1})
print(st)

# Creating a Pauli x


# Tensor XX = Pauli x with Pauli x
XX = Sigma(1).tensor(Sigma(1))
print(XX)

# Applying XX to st
print(XX*st)



# Here, we are builging the Grover Iterator: H⊗n(2|0⟩⟨0| − I)H⊗n (ref "Quantum Computation and Quantum Information" by Michael A. Nielsen & Isaac L. Chuang pg. 251)
res = Hadamard()*((2*Projection(State({'0':1}),'0')-Identity(1)) * Hadamard())
print(res)


# Here, we are builging the Grover Iterator: H⊗n(2|0⟩⟨0| − I)H⊗n (ref "Quantum Computation and Quantum Information" by Michael A. Nielsen & Isaac L. Chuang pg. 251)
res = Hadamard()*((2*Projection(State({'0':1}),'0')-Identity(1)) * Hadamard())
print(res)


# Grover search 
	# Here, we are searching for the item |0101〉in the unordered set of binary strings of size 4.

	# This is the oracle in the grover search for finding |0101〉
def oracle(st):
  st.clist['0101'] = -1*st.clist['0101']
  return st

	# The code for constructing the grover iterator	 
def grover():
	Hn = Hadamard().tensor(Hadamard().tensor(Hadamard().tensor(Hadamard())))
	G = [Hn, 2*Projection(State({'0000':1}), '0000') - Identity(4), Hn]
	st = State({'0000': 1})
	st = Hn*st
	for i in range(4):
		oracle(st)
		st = Algorithm(G)*st
	return st
print(grover())

