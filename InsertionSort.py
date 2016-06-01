#!/usr/bin/python
class InsertionSort:
	array=[0]*6
	def initialise(self):
		self.array=[5,2,3,8,1]
	def sort(self,array):
		for i in range(1,len(self.array)):
			temp=array[i]
			j=i-1
			while (j>=0 and array[j]>temp):
				array[j+1]=array[j]
				j=j-1
			array[j+1]=temp
obj=InsertionSort()
obj.initialise()
for i in range(len(obj.array)):
	print obj.array[i]
obj.sort(obj.array)
print "Sorted Array is : \n"
for i in range(len(obj.array)):
	print obj.array[i]
