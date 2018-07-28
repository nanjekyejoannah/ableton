# Author: 2018, Joannah Nanjekye

# The script has been tested with python 2.7.14 and python 3.6.3. Contact me for relevant test cases. According to 
#instructions, I was supposed to send one code file. I can send the test file if requested.
#
# Audio preview post-processing functionality
#
#****************************************************************************************

import argparse
import os

def parse_args():
	"""This parses the command line arguments that we can use later

	Returns:
		A parsed object from argparse.parse_args()
	"""
	parser = argparse.ArgumentParser(description='This CLI tool post-processes and compresses the audio rendered from the preset')
	parser.add_argument('vars', nargs='*', type=str)

	return parser.parse_args()

def main():
	"""gets parser arguments and calls function that processes the file paths provides as arguments.

	Returns:
	"""
	arguments = parse_args()
	for filePath in arguments.vars:
		try:
			process_file(filePath)
		except:
			print ("Audio preview post-processing Failed")

def process_file(filePath):
	"""Reads file from path, and runs ffmpeg command that post-processes 
	and compresses the audio files.

	Returns:
	"""

	try:
		if not os.path.exists(str(filePath)):
			print ("Warning: The filepath {0}  does not exist." .format(filePath))

		outputPath = os.path.splitext(str(filePath))[0]
		os.system("ffmpeg -y -i {0} -af atrim=duration=2 -af \
			    	acompressor=threshold=0.1:ratio=2:attack=5  -af afade=t=out:0.02 {1}.ogg". \
			    	format(filePath, outputPath))
	except IOError:
		print ("The file does not exist")
	else:
		print ("An error was encountered while processing the audio file")
	finally:
		print ("Done processing the file")

if __name__ == '__main__':
	main()