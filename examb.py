# def probTest(limit):
# 	i = 1
# 	prob = 1.0 / 6
# 	while prob > limit:
# 		prob = float((5 ** i)) / (6 ** (i + 1))
# 		i += 1
# 	return i

# print probTest(0.11)
import pylab, random
def LV(): 
	count = 0 
	while random.random() > 0.5: 
		count +=1
	return count 

histogram = [ 0 for i in range(1,1000)] 
for i in range(100): 
	result = LV()
	histogram[ result ] += 1
	print result

pylab.plot( histogram )
pylab.xlim([0, 10])
pylab.show()
