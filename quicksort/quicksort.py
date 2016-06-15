import math
import random

def createList(size):
	ret = []
	for x in range(0, size):
		ret.insert(0, math.ceil(random.random() * 100))

	return ret

def quickSort(unsortedList):
	index = unsortedList.__len__() - 1  #maybe try the medians technique later
	if (index < 1):
		return unsortedList
	pivotValue = unsortedList[index]

	lowList = []
	highList = []
	pivots = []
	for e in unsortedList:
		if (e < pivotValue):
			lowList.append(e)
		elif (e > pivotValue):
			highList.append(e)
		else:
			pivots.append(e)

	lowList = quickSort(lowList)
	highList = quickSort(highList)

	return lowList + pivots + highList
	
def swap(lst, swapA, swapB):
	temp = lst[swapA]
	lst[swapA] = lst[swapB]
	lst[swapB] = temp

toBeSorted = createList(20)
print toBeSorted
result = quickSort(toBeSorted)
print result
