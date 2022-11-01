# Purpose: move files from one directory to another
import os
import shutil

# print working directory
# dir_path = os.path.dirname(os.path.realpath(__file__))

source = '/Users/carlosgomez/Desktop/TestMoveFiles/Source'
destination = '/Users/carlosgomez/Desktop/TestMoveFiles/Destination'

# gather all files
allfiles = os.listdir(source)

# iterate on all files to move them to destination folder
for f in allfiles:
	if '.txt' in f:
		src_path = os.path.join(source, f)
		dst_path = os.path.join(destination, f)
		os.rename(src_path, dst_path)
	else:
		print("not a text file")
  