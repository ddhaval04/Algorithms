#!/usr/bin/python
class MergeSort:
	arr=[0]*6
	def initialise(self):
		self.arr=[1,3,5,2,4,6]
	def mergesort(self,arr,left,right):
		if left<right:
			mid=(left+right)/2
			self.mergesort(arr,left,mid)
			self.mergesort(arr,mid+1,right)
			self.merge(arr,left,mid,right) 
	def merge(self,arr,left,mid,right):
		n1=mid-left+1
		n2=right-mid
		Left=[0]*(n1)
		Right=[0]*(n2)
		for i in range(0,n1):
			Left[i]=arr[left+i]
		for j in range(0,n2):
			Right[j]=arr[mid+1+j]
		i=0
		j=0
		k=left
		while i<n1 and j<n2:
			if Left[i]<=Right[j]:
				arr[k]=Left[i]
				k+=1
				i+=1
			else:
				arr[k]=Right[j]
				k+=1
				j+=1
		while i<n1:
			arr[k]=Left[i]
			k+=1
			i+=1
		while j<n2:
			arr[k]=Right[j]
			k+=1
			j+=1

#Test Code:
obj=MergeSort()
obj.initialise()
n=len(obj.arr)
temp=obj.arr
print("Given array is : ")
for i in range(n):	
	print("%d"%obj.arr[i]),
obj.mergesort(temp,0,n-1)
print("\n\nSorted array is : ")
for i in range(n):
	print("%d"%obj.arr[i]),

