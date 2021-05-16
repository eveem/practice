list = [99, 2, 14, 505, 1]

def selectionSort(list):
	total = len(list)
	for i in range(0, total):
		min = list[i]
		minPose = i
		
		for j in range(i, total):
			if list[j] < min:
				min = list[j]
				minPose = j

		number = list[minPose]
		list[minPose] = list[i]
		list[i] = number

print "Before sort list = " + str(list)
selectionSort(list)
print "After sort list  = " + str(list)