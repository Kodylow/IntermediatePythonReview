# Given a circular list of gas stations, where we can go from station i to i+1 and from n back to 0, find the index of the station from where we start to be able to traverse all the stations and go back to the original station without running out of gas.

# Notes:
# We can only move forward
# the gas tank starts empty
# gas[i] represents the amount of gas at the station i
# cost[i] represents the cost to go from station i to station i+1
# the answer is guaranteed to be unique
# if the station we're searching for doesn't exist, return -1

# Pseudocode for Naive Solution
# For each station i
#    Start traversing
#    If the car goes back to i
#      i is the right station, return it

def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True

# O(n^2) Time Complexity
# O(1) Space Complexity
def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1        

# Optimized solution: if a station `start` reaches a negative amount at the index i, then all stations between start and i incusive are invalid, we start again from i + 1
# Time Complexity reduces to O(n)
def gas_station_optimized(gas, cost):
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i+1
            prev_remaining += remaining
            remaining = 0
    if candidate == len(gas) or remaining+prev_remaining < 0:
        return -1
    else:
        return candidate
    