import re, sys

#I apologize in advance for apsolutely abysmal casts in my script

#get area
def get_area(l,w,h):
	return 2*l*w + 2*w*h + 2*h*l

#parse dimensions, if given lxwxh
def get_dimensions(nonparsed):
	return re.match(r'^(.*)x(.*)x(.*)$', nonparsed).group(1,2,3)

def get_min_side(l,w,h):
	return min(l*w, w*h,l*h)

def get_wrapping_area(lwh):
	return get_area(int(lwh[0]),int(lwh[1]),int(lwh[2])) + get_min_side(int(lwh[0]),int(lwh[1]),int(lwh[2]))
#Input has everything in immoral imperial units, unfortunately.
#Fortunately, that's irrelevant for this code

def get_volume(lwh):
	return int(lwh[0]) * int(lwh[1]) * int(lwh[2])

def get_ribbon_len(lwh):
	return 2*sum(sorted([int(x) for x in lwh])[0:2]) + get_volume(lwh)

def main():
	result_area = 0
	ribbon_len = 0
	for line in open(sys.argv[1]).readlines():
		result_area = result_area + get_wrapping_area(get_dimensions(line))
		ribbon_len = ribbon_len + get_ribbon_len(get_dimensions(line))
	print result_area
	print ribbon_len



if __name__=='__main__':
	main()

