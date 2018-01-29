#!/usr/bin/env python3
'''
Copyright <2018> <Danny Antaki>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
__version__='0.0.1'
from pyfreq.vcf import allele_freq
from argparse import RawTextHelpFormatter
from time import time
import argparse,os,shutil,sys
__useage___="""
________   __  ___________ _____ _____ 
| ___ \ \ / /    ___| ___ \  ___|  _  |
| |_/ /\ V /  | |_  | |_/ /  |__| | | |
|  __/  \ /   |  _| |    /|  __|| | | |
| |     | |   | |   | |\ \| |___\ \/' /
\_|     \_/   \_|   \_| \_\____/ \_/\_\
                                     
pyfreq: compute allele frequency for VCF files
Version {}    Author: Danny Antaki <dantaki at ucsd dot edu>    github.com/dantaki/pyfreq

  pyfreq   -v <in.vcf>   -f <in.fam> [-LoPh]

input arguments: 
 
  -v, -vcf       PATH     vcf file  
  -f, -fam       PATH     plink fam file
 
optional arguments:
  
  -L, -log       PATH    log file for standard error messages [default: STDOUT]
  -o, -out       PATH    output prefix [default: pyfreq.out]
  -P, -prog              display a progress bar

  -h, -help              show this message and exit

""".format(__version__)
def main():
	init_time = int(time())
	parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,usage=__useage___,add_help=False)
	in_args, opt_args = parser.add_argument_group('input arguments'),parser.add_argument_group('optional arguments')
	in_args.add_argument('-v','-vcf',type=str,default=None,required=True)
	in_args.add_argument('-f','-fam',type=str,default=None,required=True)
	opt_args.add_argument('-L','-log',default=None,required=False)
	opt_args.add_argument('-o','-out',required=False,default="pyfreq.out",type=str)
	opt_args.add_argument('-P','-prog',required=False,default=False,action="store_true")
	opt_args.add_argument('-h','-help',required=False,action="store_true",default=False)
	args = parser.parse_args()
	vcf,fam = args.v,args.f
	logfh, ofh, prog = args.L,args.o,args.P
	_help = args.h
	if (_help==True or len(sys.argv)==1):
		print(__useage___)
		sys.exit(0)
	if fam==None:
		print('\nFATAL ERROR: fam file required\n')
		sys.exit(1)
	if vcf==None:
		print('\nFATAL ERROR: vcf file required\n')
		sys.exit(1)
	if logfh!=None:
		lfh = open(logfh,'w')
		sys.stderr=lfh
	allele_freq(fam,vcf,ofh,prog)
	# load founders
	# parse VCF
	# calculate allele freq
if __name__=='__main__': main()