group_travel_optimization
=========================

Planning a trip for a group of people (e.g. family members) from different locations all arriving at the same place through optimization. The family members are all over the country and wish to meet at New York. They will arrive on the same day and leave on the same day. They will share transportation from and to the airport. 


Structure of program
--------------------

The python program can be divided into the following:

1) The flight data are available in schedule.txt. It contains origin, destination, departure time, arrival time and price.

2) group_travel_optimization.py covers the code that parse the flight data and compute the cost (including time in air and waiting time).

3) Different optimization techniques:
	- random_search
	- hill_climbing
	- simulated_annealing
	- genetic_algorithm

These individual files will call group_travel_optimization.py and perform iterations to find the most optimum solution (i.e. with lowest overall cost, and least time spent)

How to run
----------

You can run one of these files on the terminal, and it will generate the schedule for all the family members.



Code is based on the work in Programming Collective Intelligence by Toby Segaran
