# pyfreq
cython optimized allele frequency calculation for VCFs

---

## install

```
$ pip install pyfreq
```

## usage 

```
________   __  ___________ _____ _____ 
| ___ \ \ / /    ___| ___ \  ___|  _  |
| |_/ /\ V /  | |_  | |_/ /  |__| | | |
|  __/  \ /   |  _| |    /|  __|| | | |
| |     | |   | |   | |\ \| |___\ \/' /
\_|     \_/   \_|   \_| \_\____/ \_/\_                                     
pyfreq: compute allele frequency for VCF files
Version 0.0.1    Author: Danny Antaki <dantaki at ucsd dot edu>    github.com/dantaki/pyfreq

  pyfreq   -v <in.vcf>   -f <in.fam> [-LoPh]

input arguments: 
 
  -v, -vcf       PATH     vcf file  
  -f, -fam       PATH     plink fam file
 
optional arguments:
  
  -L, -log       PATH    log file for standard error messages [default: STDOUT]
  -o, -out       PATH    output prefix [default: pyfreq.out]
  -P, -prog              display a progress bar

  -h, -help              show this message and exit
```
