from Operator import *
from State import *
from ComplexNum import *


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


#Grover search

