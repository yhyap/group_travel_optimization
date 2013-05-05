import group_travel_optimization as gto
import random

def hillclimb(domain, costf):
    """An iterative optimization method that starts with a random solution and 
     then attempts to find a better solution by incrementally changing a 
     single element of the solution"""
     # Create random solution
     sol = [random.randint(domain[i][0],domain[i][1])
             for i in range(len(domain))]
    
    # Main loop
    while 1:
        
        # Create a list of neighbouring solution
        neighbours = []
        for j in range(len(domain)):
            
            # One away in each direction
            if sol[j] > domain[j][0]:
                neighbours.append(sol[0:j] + [sol[j]+1] + sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbours.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
        
        # See what the best solution amongst the neighbour is
        current = costf(sol)
        best = current
        for j in range(len(neighbours)):
            cost = costf(neighbours[j])
            if cost < best:
                best = cost
                sol = neighbours[j]
        
        # If there is no improvement, then we have reached the top
        if best == current:
            break
    
    return sol
    