import group_travel_optimization as gto
import random

def hillclimb(domain, costf):
    """An iterative optimization method that starts with a random solution and 
     then attempts to find a better solution by incrementally changing a 
     single element of the solution"""
     # Create random solution
    sol = [random.randint(domain[i][0],domain[i][1])
             for i in range(len(domain))]   
             # e.g.: [1,4,3,2,7,3,6,3,2,4,5,3]
    
    # Main loop
    while 1:        # while true
        
        # Create a list of neighbouring solution
        neighbours = []
        for j in range(len(domain)):
            
            # Find the nearest neighbour, one away in each direction
            # Create a list with (each element in the list) of the list raised by one
            if sol[j] > domain[j][0]:
                neighbours.append(sol[0:j] + [sol[j]+1] + sol[j+1:])
            # Create a list with (each element in the list) of the list reduced by one
            if sol[j] < domain[j][1]:
                neighbours.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
        
        # See what the best solution amongst the neighbour is
        current = costf(sol)
        best = current
        for j in range(len(neighbours)):    # Go through the neighbours list
            cost = costf(neighbours[j])
            if cost < best:
                best = cost
                sol = neighbours[j]         # Tracks the sol with lowest cost
        
        # If there is no improvement, then we have reached the top
        if best == current:
            break
        
        # If best != current, the new sol will be used to loop again
    
    return sol


# There are nine outbound and inbound flights respectively for every person
# so the domain in the list is set to (min,max) repeated for each person
domain = [(0,8)]*(len(gto.people)*2)    # [(0,8), (0,8), ..., ]

# Optimizing
s = hillclimb(domain, gto.schedulecost)
print s

# Pull the data and present
gto.schedulecost(s)
gto.printschedule(s)


# Example case
# sol = [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
# neighbours = 
# [[2, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [0, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 5, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 3, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 4, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 2, 2, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 3, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 1, 7, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 8, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 6, 3, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 4, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 2, 6, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 7, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 5, 3, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 4, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 2, 2, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 3, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 1, 4, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 5, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 3, 5, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 6, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 4, 3], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 4], 
#  [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 2]]