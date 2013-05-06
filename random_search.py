# Randomly trying different solution and track the solution with the 
# lowest cost


import group_travel_optimization as gto
import random

def randomoptimize(domain,costf):
    """A random optimization method that returns a list of 2-tuple (outbound, return)
    trip that each passenger should take. The domain parameter (list of 2-tuple) 
    specify the minimum and maximum values for each variable. The costf parameter
    is the cost function obtained from schedulecost"""
    best = 999999999            # Set the initial cost to a high value
    bestr = None                # tracks the best random number generated
    for i in range(1000):
        # Create random solution
        r = [random.randint(domain[i][0],domain[i][1])
            for i in range(len(domain))]
        
        # Get the cost
        cost = costf(r)
        
        # Compare with the best so far
        if cost < best:
            best = cost
            bestr = r
    
    return r


# There are nine outbound and inbound flights respectively for every person
# so the domain in the list is set to (0,8) repeated twice for each person
domain = [(0,8)]*(len(gto.people)*2)    # [(0,8), (0,8), ..., ]

# Optimizing
s = randomoptimize(domain, gto.schedulecost)
print s         # print the list

# Pull the data and present
gto.schedulecost(s)
gto.printschedule(s)


