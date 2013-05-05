"""An optimization problem: To plan a trip for a group of people from different 
locations all arriving at the same place - New York. They will arrive on the 
same day and leave on the same day"""

# Typical data from 'schedule.txt' looks like
# LGA,MIA,20:27,23:42,169
# MIA,LGA,19:53,22:21,173
# LGA,BOS,6:39,8:09,86
# BOS,LGA,6:17,8:26,89
# LGA,BOS,8:23,10:28,149
# where they represent origin, destination, departure time, arrival time, and price


import time
import random
import math

# Define the people and their origin
people = [('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt', 'MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')]
          
# LaGuardia airpot in New York
destination = 'LGA'




# Load data from schedule.txt into a dictionary
flights = {}

# Break each line of entry into the desired data structure (i.e. dictionary)
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip().split(',')
    flights.setdefault((origin,dest),[])
    
    # Add details to the list of possible flights
    flights[(origin,dest)].append((depart,arrive,int(price)))
    
    # Eventually the dictionary will become, for example
    # {('LGA', 'MIA'): [('20:27', '23:42', 169)]}
    



# HANDY functions
def getminutes(t):
    """Compute how many minutes into the day a given time is"""
    x=time.strptime(t,'%H:%M')  # Return in the format of YYYY,MM,DD,HH,MM,SS,...
    return x[3]*60+x[4]         # Therefore will yield total minutes
    

def printschedule(r):
    """A handler that prints the flight that people will take 
    (after optimization) in a table. r is a list with numbers that
    represent which flight a person will take. For example
    r = [1,4,3,2,7,3,6,3,2,4,5,3] represents person[0] will take
    flight[1] for outbound and flight[4] for return and so on"""
    for d in range(len(r)/2):                       # as they come in pairs
        name = people[d][0]                         # e.g. 'Seymour' 
        origin = people[d][1]                       # e.g. 'BOS'
        out = flights[(origin,destination)][r[d]]   # i.e. [('8:04','10:11', 95)]
        ret = flights[(destination,origin)][r[d+1]] # format same as above
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin, 
                                                      out[0],out[1],out[2],
                                                      ret[0],ret[1],ret[2])
                                                      

def schedulecost(sol):
    """Compute the total cost of the trip and the total time spent waiting at 
    the airports for various passengers. sol is a list of trip specified
    (outbound, return). e.g. sol = [1,4,3,2,7,3,6,3,2,4,5,3]"""
    
    totalprice = 0
    latestarrival = 0
    earliestdep = 24*60
    
    # Go through each pair of return flight and track the latest arrival and earliest dep given the passenger
    for d in range(len(sol)/2):
        # Get the inbound and outbound flight
        origin = people[d][1]                                   # Get the origin of passenger
        outbound = flights[(origin,destination)][int(sol[d])]   # i.e. [('8:04','10:11', 95)]
        returnf = flights[(destination,origin)][int(sol[d+1])]  # format same as above
        
        # Total price is the price of all outbound and return flights
        totalprice += outbound[2]
        totalprice += returnf[2]
        
        # Track the latest arrival and earliest departure
        if latestarrival < getminutes(outbound[1]):
            latestarrival = getminutes(outbound[1])
        if earliestdep > getminutes(returnf[0]):
            earliestdep = getminutes(returnf[0])
    
    
    # Every person must wait at the airport until the latest person arrives
    # They also must arrive at the same time to wait for their flight
    totalwait = 0
    
    # Go through each pair of return flight and track the least total waiting time
    for d in range(len(sol)/2):
        origin = people[d][1]
        outbound = flights[(origin,destination)][int(sol[d])]
        returnf = flights[(destination,origin)][int(sol[d+1])]
        totalwait += latestarrival - getminutes(outbound[1])
        totalwait += getminutes(returnf[0]) - earliestdep
    
    
    # Does this solution requires an extra day of car rental? That'll be $50
    if latestarrival > earliestdep:
        totalprice += 50
    
    return totalprice + totalwait # assuming each minute cost $1
    


    
    
    