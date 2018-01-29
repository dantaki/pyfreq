from Cython.Build import cythonize
from setuptools import setup,Extension
import numpy
setup(
	name='pyfreq',
	version='0.0.2',
	url='https://github.com/dantaki/pyfreq',
	author='Danny Antaki',
	author_email='dantaki@ucsd.edu',
	packages=['pyfreq'],
	package_dir={'pyfreq': 'pyfreq/'},
	ext_modules=cythonize([
		Extension('pyfreq.vcf',['pyfreq/vcf.pyx']),
		],
		compiler_directives={
			'boundscheck': False,
			'wraparound': False,
			'cdivision': True,
			'language_level': 3,
		}),
	include_dirs=[numpy.get_include()],
	include_package_data=True,
	scripts= ['pyfreq/pyfreq']

)
