import argparse
import os

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('vars', nargs='*', type=str)
arguments = parser.parse_args()

def main():
	for argument in arguments.vars:
		try:
			process_file(argument)
		except:
			print ("Post processing failed")

def process_file(filePath):
	try:
		if not os.path.exists(str(filePath)):
			print ("Warning: The filepath {0}  does not exist." .format(filePath))
		    
		os.system("ffmpeg -y -i {0} -af atrim=duration=2 -af \
			    	acompressor=threshold=0.1:ratio=2:attack=5  -af afade=t=out:0.02 {0}.ogg".format(filePath))
		print ("succ")
	except IOError:
		print ("The file does not exist, exiting gracefully")
	finally:
		print ("Done processing the file")

if __name__ == '__main__':
	main()