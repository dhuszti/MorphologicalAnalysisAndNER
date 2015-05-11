# -*- coding: utf-8 -*-
import os, sys, getopt
import subprocess
from os.path import expanduser

def main(argv):
	inputfile = ''
	outputfile = ''

  	try:
		opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
  	except getopt.GetoptError:
		print 'hunpos.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
  	for opt, arg in opts:
		if opt == '-h':
	 		print 'hunpos.py -i <inputfile> -o <outputfile>'
	 		sys.exit()
		elif opt in ("-i", "--ifile"):
	 		inputfile = arg
		elif opt in ("-o", "--ofile"):
	 		outputfile = arg


	# current working directory
	homepath = os.getcwd()

	# huntoken xml output
	cmd_huntoken = 'python huntoken.py -i ' + inputfile + ' -o ' + homepath + '/huntoken.xml' 
	p = subprocess.Popen(cmd_huntoken, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# huntoken xml out to new lines
	cmd_xml2lines = 'python xml2lines.py -i ' + homepath + '/huntoken.xml -o ' + homepath + '/hunmorph_in.txt' 
	p = subprocess.Popen(cmd_xml2lines, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# szegedNER
	cmd_szegedNER = 'python szegedNER.py -i ' + inputfile + ' -o ' + homepath + '/szegedNER.txt'
	p = subprocess.Popen(cmd_szegedNER, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# hunmorph
	cmd_hunmorph = 'python hunmorph.py -i ' + homepath + '/hunmorph_in.txt -o ' + homepath + '/hunmorph_out.txt --afffile /home/hd/Desktop/morphdb.hu/morphdb_hu.aff --dicfile /home/hd/Desktop/morphdb.hu/morphdb_hu.dic'
	p = subprocess.Popen(cmd_hunmorph, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# hunpos
	cmd_hunpos = 'python hunpos.py -i ' + homepath + '/hunmorph_in.txt -o ' + homepath + '/hunpos_ki.txt --modfile /usr/local/bin/hu_szeged_kr.model --hptfile /home/hd/Desktop/hunpos-1.0-linux/hunpos-tag'
	p = subprocess.Popen(cmd_hunpos, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# morph determination
	cmd_morph = 'python morph_decision.py --posfile ' + homepath + '/hunpos_ki.txt --morphfile ' + homepath + '/hunmorph_out.txt --ofile ' + homepath + '/morph.txt'
	p = subprocess.Popen(cmd_morph, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# NER and morph determination in a file - input for sentiment analysis
	cmd_nermorph = 'python NER_and_morph_connection.py --nerfile ' + homepath + '/szegedNER.txt --morphfile ' + homepath + '/morph.txt -o ' + outputfile
	p = subprocess.Popen(cmd_nermorph, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()

	# Deleting not necesseraly files
	os.remove(homepath + '/huntoken.xml')
	os.remove(homepath + '/hunmorph_in.txt')
	os.remove(homepath + '/hunmorph_out.txt')
	os.remove(homepath + '/hunpos_ki.txt')
	os.remove(homepath + '/morph.txt')
	os.remove(homepath + '/szegedNER.txt')

if __name__ == "__main__":
   main(sys.argv[1:])


