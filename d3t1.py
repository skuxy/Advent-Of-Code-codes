import sys

#no constructor because y?
class Coordinates:
	x=0
	y=0
	visited = [(0,0)]
	def change_coordinates(self, direction):
		if direction == '>':
			self.x = self.x + 1
		elif direction == '<':
			self.x = self.x - 1
		elif direction == '^':
			self.y = self.y + 1
		elif direction == 'v':
			self.y = self.y - 1

	def is_visited(self):
		return (self.x,self.y) in self.visited

	def increment_passed(self):
		coords = (self.x,self.y)
		if not coords in self.visited:
			self.visited.append(coords)


def main():
	coordinates_santa = Coordinates()
	coordinates_robot = Coordinates()
	data = open(sys.argv[1]).read()
	for index in range(0, len(data), 2):
		if index > len(data) - 2: break
		coordinates_santa.change_coordinates(data[index])
		coordinates_santa.increment_passed()
		coordinates_robot.change_coordinates(data[index+1])
		coordinates_robot.increment_passed()

	print len(set(coordinates_santa.visited+ coordinates_robot.visited))

if __name__=='__main__':
	main()
