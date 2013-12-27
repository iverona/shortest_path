from file_reader import InputFileReader
from ShortestPath import ShortestPath


if __name__ == '__main__':
	finput, cities = InputFileReader().read()
	orig = raw_input("Select Origin: ")
	dest = raw_input("Select Destination: ")
	
	print ShortestPath().find(finput, s=str(orig), t=str(dest))