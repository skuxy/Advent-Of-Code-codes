import sys, re, time


def incrementLetter(letter):
	return 'a' if letter == 'z' else chr(ord(letter) + 1)

def incrementString(string):
	newstring=""
	l = len(string)
	for index in range(len(string)):
		if index == 0:
			newstring = newstring + incrementLetter(string[-1])
		elif string[l - index] is 'z': #if carry
			newstring = newstring + incrementLetter(string[-1-index])
		else:
			newstring = newstring + string[l-index-1::-1]
			break
	return newstring[::-1]

def checkconsecutives(string):
	#regexes won't help here :(
	for ind in range(len(string)-2):
			lett = string[ind] #to shorten
			if lett+string[ind+1]+string[ind+2] == lett+incrementLetter(lett)+incrementLetter(incrementLetter(lett)):
				if lett is not 'y' and lett is not 'z':
					return True
	return False

def checkiol(string):
	return False if 'i' in string or 'o' in string or 'l' in string else True

def checkpairs(string):
	return True if re.match(r'.*(.)\1.*([^1])\2.*',string) else False


def check(string):
	return True if checkpairs(string) and checkiol(string) and checkconsecutives(string) else False

def main():
	string = sys.argv[1]
	first = True
	while(True):
		if check(string) and first:
			string = incrementString(string)
			first=False
		if check(string) and not first:
			break
		else:
			string = incrementString(string)
		print string
	print string

if __name__ == "__main__":
	main()
