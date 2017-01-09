list = [9, 13, 1, 5, 66, 10]

def insertionSort(list):
	for i in range(1, len(list)):
		insertValue = list[i]
		checkPosition = i
		while checkPosition > 0 and insertValue < list[checkPosition - 1]:
			list[checkPosition] = list[checkPosition - 1]
			checkPosition -= 1
		list[checkPosition] = insertValue

print "Before sort list = " + str(list)
insertionSort(list)
print "After sort list  = " + str(list)