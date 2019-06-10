def insertionSort(A):
    for i in range(1,len(A)):
        k=i
        temp=A[i]
        while(k>0 and temp<A[k-1]):
            A[k]=A[k-1]
            k-=1
        A[k]=temp
    return A
print(insertionSort([6,2,8,10,1,4,2]))
        