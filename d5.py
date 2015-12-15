import re, sys

def surely_naughty(string):
	if re.match(r'.*((ab)|(cd)|(pq)|(xy)).*',string):
		return True
	return False

def good(string):
	if re.match(r'.*[aeiou].*[aeiou].*[aeiou].*',string):
		if re.match(r'.*(.)\1.*',string):
			return True
	print string
	return False
def good2(string):
	if re.match(r'.*(..).*\1.*',string):
		if re.match(r'.*(.).\1.*',string):
			return True
#main function
def main():
	good_ones=0
	good_ones2=0
	for string in open(sys.argv[1]).readlines():
		if good2(string):
			good_ones2=good_ones2 + 1
		if not surely_naughty(string):
			if good(string):
				good_ones=good_ones+1



	print good_ones
	print good_ones2
if __name__ == "__main__":
  main()
