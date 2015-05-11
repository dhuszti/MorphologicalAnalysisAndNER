# -*- coding: utf-8 -*-
import os, sys, getopt
import subprocess

def main(argv):
   nerfile = ''
   morphfile = ''
   ofile = ''

   try:
      opts, args = getopt.getopt(argv,"hn:m:o:",["nerfile=","morphfile=","ofile="])
   except getopt.GetoptError:
      print 'NER_and_morph_connection.py --nerfile <nerfile> --morphfile <morphfile> --ofile <outputfile>'
      sys.exit(3)
   for opt, arg in opts:
      if opt == '-h':
         print 'NER_and_morph_connection.py --nerfile <nerfile> --morphfile <morphfile> --ofile <outputfile>'
         sys.exit()
      elif opt in ("--nerfile"):
         nerfile = arg
      elif opt in ("--morphfile"):
	 morphfile = arg
      elif opt in ("--ofile"):
         ofile = arg

   NERlist = []
   i = 0

   with open(nerfile, 'r') as file1:
		for line in file1:
			if line != '\n':
			  NERlist.append(line.split()[1])
			  i+=1
   num = 0
   with open(ofile, 'w') as file_out:
	with open(morphfile, 'r') as file1:
	    	for line in file1:
			if line != '\n':
				file_out.write(line.split()[0]  + '\t' + line.split()[1] + '\t' + NERlist[num] + '\n')
				num+=1


if __name__ == "__main__":
   main(sys.argv[1:])
