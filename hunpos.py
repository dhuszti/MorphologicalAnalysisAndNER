# -*- coding: utf-8 -*-
import os, sys, getopt
import xml.etree.ElementTree as ET
import subprocess

def main(argv):
   inputfile = ''
   outputfile = ''
   modelfile = ''
   hunpostagfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:aff:dic",["ifile=","ofile=","modfile=","hptfile="])
   except getopt.GetoptError:
      print 'hunpos.py -i <inputfile> -o <outputfile> --modfile <modelfile> --hptfile <hunpostagfile>'
      sys.exit(4)
   for opt, arg in opts:
      if opt == '-h':
         print 'hunpos.py -i <inputfile> -o <outputfile> --modfile <modelfile> --hptfile <hunpostagfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("--modfile"):
         modelfile = arg
      elif opt in ("--hptfile"):
         hunpostagfile = arg

   # '/usr/local/bin/hu_szeged_kr.model'
   # '/home/hd/Desktop/hunpos-1.0-linux/hunpos-tag'
   # ht = HunposTagger(path_to_model = modelfile,  path_to_bin = hunpostagfile)
   
   cmd_hunpos = "cat "+inputfile+" | "+hunpostagfile+" "+modelfile+" > "+outputfile
   p = subprocess.Popen(cmd_hunpos, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()

if __name__ == "__main__":
   main(sys.argv[1:])
