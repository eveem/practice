list = [1, 2, 5, 7, 9, 13]

def binarySearch(list, value):
	first = 0
	last = len(list)
	n = len(list)
	found = False

	while found != True:
		mid = (first + last)/2
		if list[mid] == value:
			return mid
		elif list[mid] < value:
			first = mid + 1
		elif list[mid] > value:
			last = mid - 1
		n -= 1
		if n <= 0:
			found = True

print binarySearch(list, 0)
print "Found 13 at index " + str(binarySearch(list, 13))