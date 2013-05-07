# Genetic algorithm

import group_travel_optimization as gto
import random


def geneticoptimize(domain, costf, popsize=50, step=1, mutprob=0.2, elite=0.2, maxiter=100):
    """Create a set of initial random solution known as population. At each step
    of optimization, the cost function of the entire population is calculated to
    get a ranked list of solution. After that, a new set of next generation 
    population is created. The top solutions from ranked list will be added to 
    the new generation. The rest of the new population consists of completely 
    new solutions that are created by modifying the best solutions."""
    # popsize: size of population
    # mutprob: probability that new member will be mutation rather than crossover
    # elite: fraction of population that are considered good and allowed to pass to next generation
    # maxiter: no. of generations to run    
    
    # Mutation: small and random change to an existing solution
    def mutate(vec):
        i = random.randint(0, len(domain)-1)                # pick an index
        if random.random() < 0.5 and vec[i] > domain[i][0]: 
            return vec[0:i] + [vec[i]-step] + vec[i+1:]     # -1 to change
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i]+step] + vec[i+1:]     # +1 to change
            
    # Crossover/breeding: taking two best solutions and breed
    def crossover(r1, r2):
        i = random.randint(1, len(domain)-2)  # pick an index that will be used to split
        return r1[0:i] + r2[i:]                             # combine 
    
    # Build an initial population
    pop = []
    for i in range(popsize):
        vec = [random.randint(domain[i][0], domain[i][1]) 
            for i in range(len(domain))]
        pop.append(vec)                       # add random solutions to population
    
    # How many survivors from each generation
    topelite = int(elite*popsize)
    
    # Main loop
    for i in range(maxiter):
        scores = [(costf(v),v) for v in pop] # evaluate the cost of all solutions
        scores.sort()                        # rank according to cost
        ranked = [v for (s,v) in scores]     # only select the solutions, not cost
    
        # Start with the pure winners
        pop = ranked[0:topelite]             # select the survivors
        
        # Add mutated and bred forms from the survivors
        while len(pop) < popsize:
            if random.random() < mutprob:
                # Mutation
                m = random.randint(0, topelite)             # only choose from survivors
                pop.append(mutate(ranked[m]))
            else:
                # Crossover
                c1 = random.randint(0, topelite)            # only choose from survivors
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


# In case the code yield error: This code is working
# Just try several times and it will run


# Expected answer
# Total cost: 3533
# sol = [4, 3, 3, 3, 4, 3, 3, 0, 0, 0, 0, 0]
#   Seymour       BOS 12:34-15:02 $109 10:33-12:03 $ 74
#    Franny       DAL 10:30-14:57 $290 10:51-14:16 $256
#     Zooey       CAK 10:53-13:36 $189 10:32-13:16 $139
#      Walt       MIA 11:28-14:40 $248 12:37-15:05 $170
#     Buddy       ORD 12:44-14:17 $134 10:33-13:11 $132
#       Les       OMA 11:08-13:07 $175 11:07-13:24 $171