# The function will return the index of the elem as a zero based index
import random
import time

def binary_search(A,elem):
    length_of_array = len(A)                                        # Constant time in python https://wiki.python.org/moin/TimeComplexity
    mid_point = length_of_array/2
    if(length_of_array == 1):
        if(A[0] == elem):
            return 0
        else:
            return -1
    elif(A[mid_point] == elem):
        return mid_point
    elif(A[mid_point] < elem):
        return mid_point + binary_search(A=A[mid_point:],elem=elem)
    else:
        return binary_search(A=A[:mid_point],elem=elem)


def binary_search_randomized(A,elem):
    length_of_array = len(A)
    break_point = random.randrange(0,length_of_array)
    if(length_of_array == 1):
        if(A[0] == elem):
            return 0
        else:
            return -1
    elif(A[break_point] == elem):
        return break_point
    elif (A[break_point] < elem):
        return break_point + binary_search_randomized(A=A[break_point:], elem=elem)
    else:
        return binary_search_randomized(A=A[:break_point], elem=elem)


N_Array = [100000,1000000,10000000]
for N in N_Array:
    A = [i*5 for i in range(N)]
    nonExistentVal = [2*random.randrange(0,N+N/2) for i in range(300)]
    existingVal = [5*random.randrange(0,N) for i in range(700)]
    start = time.time()
    for i in existingVal:
        binary_search(A, i)
    for i in nonExistentVal:
        binary_search(A, i)
    end = time.time()
    print ("binary search for N= " + str(N) + "  : " + str(end-start))
    start = time.time()
    for i in existingVal:
        binary_search_randomized(A, i)
    for i in nonExistentVal:
        binary_search_randomized(A, i)
    end = time.time()
    print ("randomized search for N= " + str(N) + "  : " + str(end-start))

