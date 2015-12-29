import sys, time

#yolo for both. Globals are here JIC

global string
string = sys.argv[1]
global newString
newString=""
sys.setrecursionlimit(1000000)

def countLettrs(indx, last, numOfRepeats):
	global newString #idiotism
	global string
	if indx is len(string): return
	elif string[indx] == last:
		countLettrs(indx+1,last,numOfRepeats+1)
	else:
		newString = newString + str(numOfRepeats) + str(last) #jic
		countLettrs(indx+1, string[indx], 1)



for i in range(40):
	#time.sleep(1)
	newString=""
	try:
		countLettrs(0, string[0], 0)
	except:
		print i
		print len(newString)
	string = newString


print len(newString)
