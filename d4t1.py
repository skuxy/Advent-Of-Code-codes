import md5
import re
import sys
import time

#goal is to find minimal number which, when supplemented to given input,
#digested gives 5 leading zeros

#checked
def has_n_leading_zeros(hashed_string,n_of_zeroes=5):
	return re.match(r'0{' + n_of_zeroes + '}.*',hashed_string)
	
def find_lowest_hash(secret_key, n_of_zeroes=5):
	i = 0
	while True:
		if has_n_leading_zeros(md5.new(secret_key+str(i)).hexdigest(), n_of_zeroes):
			return i
		i = i + 1
		
def main():
	print find_lowest_hash(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	main()
