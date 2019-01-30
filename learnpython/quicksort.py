import random

arr=random.sample(range(100),5)
print(arr)


def quickSort(arr,low,high):
	if(low>=high):
		return;
	pivot=arr[high]
	index=partition(arr,low,high,pivot)
	print('array',arr)
	quickSort(arr,low,index-1)
	quickSort(arr,index+1,high)

def partition(arr,low,high,pivot):
	print(arr[low:high+1],'pivot',pivot)
	i=low
	j=high
	while i<=j:
		while arr[i]<pivot:
			i+=1
		while arr[j]>pivot:
			j-=1
		if i<=j:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
			j-=1
	print(arr[low:high+1],'low',low,'high',high,'pivot',pivot,'index',i)
	print('return index',i)
	return i

quickSort(arr,0,len(arr)-1)
print(arr)
		