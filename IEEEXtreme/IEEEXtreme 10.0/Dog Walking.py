# Number of test cases
test_cases = int(input())

for i in range(test_cases):    
    N, K = (int(n) for n in input().split(" ")) # Number of dogs and dog walkers
    
    dogs = []
    differences = []
    
    for j in range(N):
        dog_size = int(input())
        dogs.append(dog_size)
    
    dogs.sort()
        
    for j in range(0, N - 1):
        difference = dogs[j + 1] - dogs[j]
        differences.append(difference)
        
    differences.sort()
    
    weight = dogs[-1] - dogs[0]
    
    if K != 1:
        weight  -= sum(differences[-(K -1 ):])      
        
    print(weight)
