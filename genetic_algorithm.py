# Genetic algorithm

import group_travel_optimization as gto
import random


def geneticoptimize(domain, costf, popsize=50, step=1, mutprod=0.2, elite=0.2, maxiter=100):
    """Create a set of initial random solution known as population. At each step
    of optimization, the cost function of the entire population is calculated to
    get a ranked list of solution. After that, a new set of next generation 
    population is created. The top solutions from ranked list will be added to 
    the new generation. The rest of the new population consists of completely 
    new solutions that are created by modifying the best solutions."""
    
    # Mutation: small and random change to an existing solution
    def mutate(vec):
        i = random.randint(0, len(domain)-1)                # pick an index
        if random.random() < 0.5 and vec[i] > domain[i][0]: 
            return vec[0:i] + [vec[i]-step] + vec[i+1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i]+step] + vec[i+1:]
            
    # Crossover/breeding: taking two best solutions and breed
    def crossover(r1, r2):
        i = random.randint(1, len(domain)-2)
        return r1[0:i] + r2[i:]
    
    # Build an initial population
    pop = []
    for i in range(popsize):
        vec = [random.randint(domain[i][0], domain[i][1]) 
            for i in range(len(domain))]
        pop.append(vec)
    
    # How many winners from each generation
    topelite = int(elite*popsize)
    
    # Main loop
    for i in range(maxiter):
        scores = [(costf(v),v) for v in pop]    # 
        scores.sort()
        ranked = [v for (s,v) in scores]
    
        # Start with the pure winners
        pop = ranked[0:topelite]
        
        # Add mutated and bred forms from the winners
        while len(pop) < popsize:
            if random.random() < mutprod:
                # Mutation
                m = random.randint(0, topelite)
                pop.append(mutate(ranked[m]))
            else:
                # Crossover
                c1 = random.randint(0, topelite)
                c2 = random.randint(0, topelite)
                pop.append(crossover(ranked[c1], ranked[c2]))
            
        # Print current best score
        print scores[0][0]
        
    return scores[0][1]


# There are nine outbound and inbound flights respectively for every person
# so the domain in the list is set to (0,8) repeated twice for each person
domain = [(0,8)]*(len(gto.people)*2)    # [(0,8), (0,8), ..., ]

# Optimizing
s = geneticoptimize(domain, gto.schedulecost)
print s

# Pull the data and present
gto.schedulecost(s)
gto.printschedule(s)