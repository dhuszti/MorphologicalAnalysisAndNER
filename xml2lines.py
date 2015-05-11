# -*- coding: utf-8 -*-
import os, sys, getopt
import xml.etree.ElementTree as ET
import subprocess

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'xml2lines.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'xml2lines.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

   tree = ET.parse(inputfile)
   root = tree.getroot()

   
   file_out = open(outputfile, "w")

   for body in root.getiterator('body'):
      for paragraph in body:
        if paragraph.tag == 'p':
            for sentence in paragraph:
                if sentence.tag == 's':
                    for word in sentence:
			if word.tag == 'w':
				connS = word.text
				file_out.write(connS.encode('utf8'))
			elif word.tag == 'c':
				# it is to change if you use HunTag/HunNER 
				#if word.text in ('.','!','?'):
				#	connS = word.text+'\n\n'
				#else:
				connS = word.text+'\n'
				file_out.write(connS.encode('utf8'))
   file_out.close()

if __name__ == "__main__":
   main(sys.argv[1:])
