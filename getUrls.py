# -*- coding: utf-8 -*-

import os 
from ipdb import set_trace

def GetallUrl(subdir,outfileName):
	outfile = open(outfileName,'w')
	list_dirs = os.walk(os.getcwd()+subdir)
	# set_trace()
	sum = 0
	for root, dirs,files in list_dirs:
		for f in files:
			sum = sum + 1
			if sum % 1000 == 0:
				print sum
			infile = open(os.path.join(os.getcwd()+subdir,f))
			# set_trace()
			outfile.write(infile.readline()[:-1]+'\t10\n')
			infile.close()
	outfile.close()

# GetallUrl("\cnn\\test\\","cnnTesturls.txt")
# GetallUrl("\cnn\\training\\","cnnTrainingurls.txt")
# GetallUrl("\cnn\\validation\\","cnnValidationurls.txt")
GetallUrl("\dailymail\\test\\","dailymailTesturls.txt")
GetallUrl("\dailymail\\training\\","dailymailTrainingurls.txt")
GetallUrl("\dailymail\\validation\\","dailymailValidationurls.txt")