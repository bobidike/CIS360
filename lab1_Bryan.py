import random


array= [] #empty list

# generate 1000 different numbers and add to the array  
def thousand(array, n=1000):
    while(len(array)<n): 
        array.append(random.randint(0,2*n))
    return array

# generate 100,000 random numbers in an array
def hundred_thousand(array, n=100000):
    while(len(array)<n): 
        array.append(random.randint(0,2*n))
    return array
    
def million(array, n=1000000):
    while(len(array)<n): 
        array.append(random.randint(0,2*n))
    return array
    

# array to be searched
#n is size of array
#x is integer we look for

def sequential(array,n,x):
    counter =0; # n of times list was traversed to find key
    location=1;
    while(location<=n and array[location]!= x):
        counter+=counter
        location+=location
    if(location>n):
        location =0
        return location, counter
    else:
        return location, counter

print()




# def binary():

#test
