def measure(dimensions):
        #day 1
	dimensions = [int(dimension) for dimension in dimensions.split("x")]
	lowest = [ dimensions.pop(dimensions.index(min(dimensions)))for x in range(2)]
	l = dimensions[0]
	w = lowest[0]
	h = lowest[1]
	#return 2*l*w + 3*w*h + 2*h*l
	#day 2
	return 2*w + 2*h + l*w*h
        
f = open("day2_1.txt", "r")
measures = f.readlines()
f.close()
total = 0
for dimension in measures:
    total += measure(dimension)
print total
