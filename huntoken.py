#!/usr/bin/python

import os, sys, getopt
import subprocess, tempfile
from os.path import expanduser

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'huntoken.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'huntoken.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

   # homepath of user
   homepath = expanduser("~")
 
   cmd_convert = "iconv -f UTF-8 -t ISO-8859-2 "+inputfile+" > "+homepath+"/Desktop/test_temp.txt"
   p = subprocess.Popen(cmd_convert, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   
   cmd_huntoken = "cat "+homepath+"/Desktop/test_temp.txt | huntoken > "+outputfile
   p = subprocess.Popen(cmd_huntoken, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()

   # remove temporary file
   os.remove(homepath+"/Desktop/test_temp.txt")
   

if __name__ == "__main__":
   main(sys.argv[1:])
