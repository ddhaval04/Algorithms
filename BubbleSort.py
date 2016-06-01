#!/usr/bin/python
class BubbleSort:
	array=[0]*6
	def initialise(self):
		self.array=[5,2,3,8,1]
	def sort(self,array):
		for i in range(len(array)):
			for j in range(len(array)-1,i,-1):
				if array[j]<array[j-1]:
					temp = array[j]
					array[j]=array[j-1]
					array[j-1]=temp
obj=BubbleSort()
obj.initialise()
obj.sort(obj.array)
for i in range(len(obj.array)):
	print obj.array[i]
