from timeit import default_timer as timer
f = open ('per','w')
start = timer()
start2 = counter = 0.0
for x in range(0,10):
	x += x
	start2 = timer()
	for y in range(0,100000):
		y += y
	end2 = timer()
	counter = (end2 - start2) + counter
end = timer()

f.write("First loop:"+"{0:.4f}".format(end-start)+"\n")
f.write("Second loop:"+"{0:.4f}".format(counter)+"\n")
f.write("Diff:"+"{0:.4f}".format((end-start)-counter)+"\n")
f.close()

#"{0:.2f}".format(13.949999999999999)
