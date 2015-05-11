# -*- coding: utf-8 -*-
import os, sys, getopt
import subprocess, linecache

def main(argv):
	posfile = ''
	morphfile = ''
	ofile = ''

	try:
		opts, args = getopt.getopt(argv,"hp:m:o:",["posfile=","morphfile=","ofile="])
	except getopt.GetoptError:
		print 'morph_decision.py --posfile <hunpos_out> --morphfile <hunmorph_out> --ofile <outputfile>'
		sys.exit(3)
	for opt, arg in opts:
		if opt == '-h':
			print 'morph_decision.py --posfile <hunpos_out> --morphfile <hunmorph_out> --ofile <outputfile>'
			sys.exit()
		elif opt in ("--posfile"):
			posfile = arg
		elif opt in ("--morphfile"):
			morphfile = arg
		elif opt in ("--ofile"):
			ofile = arg



	# HunMorph Word Index
	IndexList_HunMorph = []
	i = 0

	with open(morphfile, 'r') as file1:
		for line in file1:
			if line != '\n':
				if line.startswith('> '):
					IndexList_HunMorph.append(i)
					i+=1
				else:
					i+=1

	Index_HunMorph_Length = len(IndexList_HunMorph)

	i = 0

	# Decision making part
	with open(ofile, 'w') as file_out:
	   with open(posfile, 'r') as file2:
		for line in file2:
			if line != '\n':
				file_out.write(line.split()[0] + '\t')
			  	# HunPos szofaj
			  	hunpos = line.split()[1]
		
				if i < (Index_HunMorph_Length-1):
					Start = IndexList_HunMorph[i]
					End = IndexList_HunMorph[i+1]
					i+=1

				HunMorph = []
				for num in range(Start+2,End+1):

					hunmorph = linecache.getline(morphfile, num).decode('latin2').encode('utf8')
					HunMorph.append(hunmorph)
			
				if len(HunMorph) == 1:					
					if hunpos == 'NUM':
						file_out.write(hunpos + '\n')
					else:	
						file_out.write(HunMorph[0] + '\n')
				else:
					iterator = 0
					HunPosMorph = []
					# HunMorph results filter with HunPos
					for iterator in range(0,len(HunMorph)):
						if hunpos in HunMorph[iterator]:				
							HunPosMorph.append(HunMorph[iterator])
						iterator+=1
					# Filtered results' number is 0 - it can occur in case of no common det.
					if len(HunPosMorph) == 0:
						file_out.write(HunMorph[0] + '\n') 
					# Filtered results' number is 1
					if len(HunPosMorph) == 1:	
						file_out.write(HunPosMorph[0] + '\n')
					# Filtered results' number is more than 1
					elif len(HunPosMorph) > 1:
						file_out.write(HunPosMorph[1] + '\n')

if __name__ == "__main__":
   main(sys.argv[1:])
				
