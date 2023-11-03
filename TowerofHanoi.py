# Recursive Python function to solve tower of hanoi 

#move the smallest disks whill allowing the largest to be left in the correct spot
def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
	if n == 0: 
		return
	#move to a aux rod 
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 


# Driver code 
N = 5

# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 
