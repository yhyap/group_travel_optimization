# Simulated annealing
# Similar to hill climbing, if new cost is lower, current sol = new sol
# Unlike hill climbing, if cost is higher, current sol = new sol with certain probability
# Therefore avoiding local minimum problem

import group_travel_optimization as gto
import random
import math


def annealingoptimize(domain, costf, T=10000.0, cool=0.95, step=1):
    """An optimization that begins with random solution, uses a variable to
    represent temperature which starts very high, and gradually gets lower. In 
    each iteration, solution is randomly chosen and changed in certain direction. 
    The cost is calculated before and after the change, and being compared."""
    # Initialize the value randomly
    vec = [float(random.randint(domain[i][0],domain[i][1])) 
            for i in range(len(domain))]
    
    while T > 0.1:
        # Choose one of the indices
        i = random.randint(0, len(domain)-1) # pick randomly within the domain
        
        # Choose a direction to change it
        dir = random.randint(-step, step)   # random between up, down or stay same
        
        # Create a new list with one of the values changed
        vecb = vec[:]
        vecb[i] += dir
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]
        
        # Calculate the current cost and new cost
        ea = costf(vec)             # high cost
        eb = costf(vecb)            # low cost
        p = pow(math.e, (-ea-eb)/T) # probability of higher cost solution being accepted
        
        # Is it better, or does it make the probability cutoff?
        if (eb<ea or random.random()<p):
            vec = vecb
        
        # Decrease the temperature
        T = T*cool
    
    return vec


# There are nine outbound and inbound flights respectively for every person
# so the domain in the list is set to (0,8) repeated twice for each person
domain = [(0,8)]*(len(gto.people)*2)    # [(0,8), (0,8), ..., ]

# Optimizing
s = annealingoptimize(domain, gto.schedulecost)
print s

# Pull the data and present
gto.schedulecost(s)
gto.printschedule(s)