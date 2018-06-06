#!/usr/bin/python3
# Author: David Byrne
# COMP 559 CSUCI 
# bsgs.py solves for x in g^x = h % p 
# This implimentation uses a binary try and has a asymptotic bound of Nlog(N) where N = sqrt(p)
# USAGE: bsgs.py <g> <h> <p>
#        where g^x = h % p 
# Dependancies: uses pip3 to install bintrees 

import sys
from math import ceil, sqrt, floor
from bintrees import BinaryTree

def bsgs(g, h, p):

    N = 1+(floor(sqrt(p)))
    
    #Store big steps in bTree so that we can search in logn time 
    L1  = BinaryTree({pow(g, i, p) : i for i in range(N)}) 
    
    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    #Store Little Steps 
    L2 = BinaryTree({(h * pow(c, j, p)) % p: j for j in range(N)})

    for key in L2.keys():                    #O(n)
      if L1.__contains__(key):               #computed in log(n) time  
        x= (L2.get(key) * N + L1.get(key))
        print(x, "is a solution for x")
    return "Done" 
#Main entry point          
if len(sys.argv) < 4: exit("Error")
print(bsgs(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
