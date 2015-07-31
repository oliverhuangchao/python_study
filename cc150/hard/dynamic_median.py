#dynamicly get the median
import heapq
import sys
import pdb

max_heap = []
min_heap = []
ori = []
count = 0

median_low = 0
median_high = 2**31
while True:
	try:
		z = int(raw_input())
	except:
		print "finish"
		break
	ori.append(z)
	if count == 0:
		count += 1
		median_low = z
		print sorted(ori)
		print "currently the median is %d" % median_low
		continue
	if count % 2 == 0: # even case
		print sorted(ori)
		if z > median_high:
			heapq.heappush(min_heap,z)
			heapq.heappush(max_heap,(-median_low,median_low))
			median_low = median_high
			print "currently the median is %d" % median_high
		elif z < median_low:
			heapq.heappush(max_heap,(-z,z))
			heapq.heappush(min_heap,median_high)
			print "currently the median is %d" % median_low
		else:
			heapq.heappush(max_heap,(-median_low,median_low))
			heapq.heappush(min_heap,median_high)
			median_low = z
			print "currently the median is %d" % z
		
		
	else: # odd case
		if z >= median_low:
			heapq.heappush(min_heap,z)
			median_high = heapq.heappop(min_heap)
		else:
			heapq.heappush(max_heap,(-z,z))
			median_high = median_low
			median_low = heapq.heappop(max_heap)[1]
		print sorted(ori)
		res = (float(median_low)+float(median_high))/2
		print "currently the median is %f" % res
	print max_heap
	count += 1






	

