list = [99, 2, 14, 505, 1]

def selectionSort(list):
	start = 0
	total = len(list)
	for i in range(0, total):
		min = list[start]
		minPose = start
		for j in range(start, total):
			if list[j] < min:
				min = list[j]
				minPose = j
		number = list[minPose]
		list[minPose] = list[start]
		list[start] = number
		start += 1

print "Before sort list = " + str(list)
selectionSort(list)
print "After sort list  = " + str(list)