#!python
#cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True
import os,sys
from tqdm import tqdm
def allele_freq(fam,vcf,ofh,prog):
	founders = get_founders(fam)
	sample_index = index_header(vcf,founders)
	del founders
	freqs = iterate_vcf(vcf,sample_index,ofh,prog)
def ferr(f):
	if not os.path.isfile(f):
		print('FATAL ERROR {} does not exist'.format(f))
		sys.stderr.write('FATAL ERROR {} does not exist\n'.format(f))
		sys.exit(1)
def get_founders(fam):
	ferr(fam)
	founders={}
	with open(fam,'r') as f:
		for l in f:
			r = l.rstrip().split('\t')
			if r[2] == "0": founders[r[1]]=True
	return founders
cdef index_header(vcf,founders):
	cdef unsigned int ind
	index={}
	vcf_f=None
	if vcf.endswith('.gz'):
		import gzip
		vcf_f = gzip.open(vcf,'r')
	else: vcf_f = open(vcf,'r')
	with vcf_f as f:
		for l in f:
			if vcf.endswith('.gz'):
				l = l.decode("utf-8")
			r = l.rstrip().split('\t')
			if l.startswith('#CHROM'):
				for ind in range(0,len(r)):
					if founders.get(r[ind])!=None:
						index[ind]=True
			if not l.startswith('#'): break
	return index
cdef iterate_vcf(vcf,sample_index,ofh,prog):
	cdef bint terminate=0
	cdef unsigned short a=0
	cdef unsigned int ac=0
	cdef unsigned int ind=0
	#cdef float af=0.
	cdef float tot = len(sample_index)
	vcf_f=None
	out = open(ofh,'w')
	out.write('ID\tALLELE_COUNT\tALLELE_FREQUENCY\n')
	if vcf.endswith('.gz'):
		import gzip
		vcf_f = gzip.open(vcf,'r')
	else: vcf_f = open(vcf,'r')
	with vcf_f as f:
		tq = tqdm(total=os.path.getsize(vcf),unit='B',unit_scale=True,disable= not prog, file=sys.stdout)
		for l in f:
			tq.update(len(l))
			if vcf.endswith('.gz'):
				l = l.decode("utf-8")
			r = l.rstrip().split('\t')
			if not l.startswith('#'):
				########################
				a=0
				ac=0
				for ind in sample_index:
					gt = r[ind].split(':').pop(0).replace("|","/")
					if '.' in gt: continue
					for allele in gt.split('/'):
						a = int(allele)
						if a > 1: terminate=1
						ac+=a
				if terminate==0:
					out.write("{}\t{}\t{}\n".format(r[2],ac,ac/(2*tot)))
				else: sys.stderr.write('WARNING: multiallelic variant found {}\n'.format(r[2]))