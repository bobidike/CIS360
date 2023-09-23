import random

a=[-2,-4,3,-1,5,6,-7,-2,4,-3,2]
A=[4,1,-9,0,2,-1,9,-6,-3,8] # example n book

B= [-2,3,4,1]


def MaxsubSlow(A):
    m=0 #subarraysum
    counter =0
    for j in range(0,len(A)):
        for k in range(j, len(A)):
            s=0 #next partial sum
            for i in range(j,k):
                counter+=1
                s=s+A[i]
            if s>m:
                m=s

    return m

def MaxsubFaster(A):
    #initialise array w all zeroes same size as array A
    S=[0]*len(A)
    counter =0 

    for i in range(0, len(A)):
        counter+=1
        S[i]= S[i-1]+A[i]
    m=0 # the max found so far
    
    for j in range(0, len(A)):
        for k in range(j, len(A)):
            counter+=1
            s= S[k]-S[j-1]
            if s > m:
                m=s
    return m


def MaxsubFastest(A):
    counter= 0
    M=[0]*len(A)

    for t in range(0, len(A)):
        counter+=1
        M[t]= max(0, M[t-1]+A[t])
    m=0
    for t in range(0,len(A)):
        counter+=1
        m= max(m, M[t])
    return m


#n is size of array
def arrayGenerator(n):
    # create and initialise elements in array with 0

    #loop through array replace 0 with random number generated till pos n-1

print(MaxsubFastest(a))

