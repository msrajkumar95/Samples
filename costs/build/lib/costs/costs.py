from itertools import permutations

def find_total_cost(busCosts, minCost):
    totalCost = 0
    previousCost = 0
    for i in range(1, len(busCosts)):
        if i==1:
            previousCost = busCosts[i - 1] + busCosts[i]
        else:
            previousCost += busCosts[i]
        totalCost += previousCost
        print(sum(busCosts,i))
        if totalCost + sum(busCosts[i+1:]) >= minCost:
            return totalCost
    return totalCost
    
def find_minimum_cost():
	costs = [6,5,9,4]
		
	minCost = 1000000000000000
	s = set()
		
	for values in permutations(costs):
		if values not in s:
			s.add(values)
			cost = find_total_cost(values, minCost)
			if cost < minCost: minCost = cost
		
	print(minCost)
