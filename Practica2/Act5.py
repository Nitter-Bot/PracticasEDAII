import math as mt

#Left heap
def h_izq(i):
    return i*2+1

#Right heap
def h_der(i):
    return i*2+2

#Swap
def swap(A,i,j):
    A[i],A[j] = A[j],A[i]

#Get Min heapify
def min_heapify(A,i,n):
    L = h_izq(i)
    R = h_der(i)
    
    posMin = L if (L<n and A[L]<A[i]) else i

    if (R < n and A[R]<A[posMin]):
        posMin=R

    if(posMin !=i):
        swap(A,i,posMin)
        min_heapify(A,posMin,n)


#Construction of heap
def createHeap(A,n):
    for i in range(mt.ceil((n-1)/2),-1,-1):
        min_heapify(A,i,n)
    print("Heap min inicial")
    print(*A)
#Sort the heap       
def HeapSort(A,n,x):
    createHeap(A,n)
    print("\nInicia Heap Sort\n")
    for i in range(n-1,-1,-1):
        swap(A,0,i)
        n-=1
        min_heapify(A,0,n)

if __name__ == "__main__":
    secuencia = [10,14,16,8,9,7,1,2,4,3]
    n = x = len(secuencia)
    print(*secuencia)
    HeapSort(secuencia,n,x)
    print(*secuencia)
