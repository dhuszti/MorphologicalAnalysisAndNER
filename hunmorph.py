# -*- coding: utf-8 -*-
import os, sys, getopt
import xml.etree.ElementTree as ET
import subprocess
from os.path import expanduser

def main(argv):
   inputfile = ''
   outputfile = ''
   aff_file = ''
   dictionaryfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:aff:dic",["ifile=","ofile=","afffile=","dicfile="])
   except getopt.GetoptError:
      print 'hunmorph.py -i <inputfile> -o <outputfile> --afffile <aff_file> --dicfile <dictionaryfile>'
      sys.exit(4)
   for opt, arg in opts:
      if opt == '-h':
         print 'hunmorph.py -i <inputfile> -o <outputfile> --afffile <aff_file> --dicfile <dictionaryfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("--afffile"):
         aff_file = arg
      elif opt in ("--dicfile"):
         dictionaryfile = arg

   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   print 'Aff file is "', aff_file
   print 'Dic file is "', dictionaryfile

   # homepath of user
   homepath = expanduser("~")

   cmd_convert = "iconv -f UTF-8 -t ISO-8859-2 "+inputfile+" > "+homepath+"/Desktop/test_temp.txt"
   p = subprocess.Popen(cmd_convert, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()

   # /home/hd/Desktop/morphdb.hu/morphdb_hu.aff
   # /home/hd/Desktop/morphdb.hu/morphdb_hu.dic

   cmd_hunmorph = "cat "+homepath+"/Desktop/test_temp.txt"+" | ocamorph --aff "+aff_file+" --dic "+dictionaryfile+" > "+outputfile
   p = subprocess.Popen(cmd_hunmorph, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()

   os.remove(homepath+"/Desktop/test_temp.txt")

if __name__ == "__main__":
   main(sys.argv[1:])
