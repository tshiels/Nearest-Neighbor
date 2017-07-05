import sys
from math import sqrt
import re
import time

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

def dist(p1, p2):
	return sqrt(pow(float(p1[0])-float(p2[0]),2) + pow(float(p1[1])-float(p2[1]),2))

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points):

	L = []
	R = []
	#change strings to floats and sorts by x value
	points = sorted(points, key=lambda x: float(x[0]))


	if len(points) <= 3:
		return brute_force_nearest_neighbor(points)


	#divide size of array into half, get midpoint
	med = int(len(points) // 2)
	#p_med = float(points_numbers[med]) #GOT RID OF SECOND [0] after [med]


	#split into left and right sides
	for i in range(0, med):
		L.append(points[i])
	for j in range(med+1, len(points)):
		R.append(points[j])


	dl = nearest_neighbor(L)
	dr = nearest_neighbor(R)

	
	d = min(dl, dr)
	
	#strip away distances greater than d
	j = 0
	strip = [None] * len(points)
	for k in range(0, len(points)):
		if (float(points[k][0]) > med - d) or (float(points[k][0]) < med + d):
			strip[j] = points[k]
			j+=1

	#sort by y coord
	strip = sorted(strip, key=lambda x: float(x[1]))
	strip_closest = brute_force_nearest_neighbor(strip)
	#return nearest_neighbor_recursion(points)
	return min(d, strip_closest)

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):
	min_distance=999999
	for i in range(0, len(points)):
		for j in range(i + 1, len(points)):
			if dist(points[i], points[j]) < min_distance:
				min_distance = dist(points[i], points[j])
	return min_distance

def nearest_neighbor_recursion(points):
	min_distance=9999

	return min_distance

def read_file(filename):
	points=[]
	# File format
	# x1 y1
	# x2 y2
	# ...
	in_file=open(filename,'r')
	for line in in_file.readlines():
		line = line.strip()
		point_match=pointRE.match(line)
		if point_match:
			x = point_match.group(1)
			y = point_match.group(2)
			points.append((x,y))
	print(points)
	return points

def main(filename,algorithm):
	algorithm=algorithm[0:]
	points=read_file(filename)
	if algorithm =='dc':
		#print("Divide and Conquer: ", nearest_neighbor(points))
		start_time = time.time()
		with open("%s_distance.txt" % (filename[:-4]), "w") as text_file:
			print("Divide and Conquer: {}".format(nearest_neighbor(points)), file=text_file)
		print("time: ", 1000*(time.time() - start_time), "milliseconds")
	if algorithm == 'bf':
		#print("Brute Force: ", brute_force_nearest_neighbor(points))
		start_time = time.time()
		with open("%s_distance.txt" % (filename[:-4]), "w") as text_file:
			print("Brute Force: {}".format(brute_force_nearest_neighbor(points)), file=text_file)
		print("time: ", 1000*(time.time() - start_time), "milliseconds")
	if algorithm == 'both':
		#print("Divide and Conquer: ", nearest_neighbor(points))
		#print("Brute Force: ", brute_force_nearest_neighbor(points))
		start_time = time.time()
		with open("%s_distance.txt" % (filename[:-4]), "w") as text_file:
			print("Divide and Conquer: {}".format(nearest_neighbor(points)), file=text_file)
			second_time = time.time()
			print("Brute Force: {}".format(brute_force_nearest_neighbor(points)), file=text_file)
			third_time = time.time()
		print("Divide and Conquer time: ", 1000*(second_time - start_time), "milliseconds")
		print("Brute Force time: ", 1000*(third_time - second_time), "milliseconds")

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("python assignment1.py -<dc|bf|both> <input_file>")
		quit(1)
	if len(sys.argv[1]) < 2:
		print("python assignment1.py -<dc|bf|both> <input_file>")
		quit(1)
	main(sys.argv[2],sys.argv[1])
