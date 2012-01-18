#!/usr/bin/env python

# 
# Copyright (C) 2010-2011 Platform Computing
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
# 
from distutils.core import setup, Extension

setup(name='platform-python-lsf-api',
      version='0.0.1',
      description='Python binding for Platform LSF APIs',
      license='LGPL',
      keywords='LSF,Grid,Cluster,HPC',
      url='http://www.platform.com',
      ext_package='platform-lsf',
      ext_modules=[Extension('_lsf', ['platform-lsf/lsf.i'],
                               include_dirs=['/usr/include/python2.6'],
                               library_dirs=['/opt/platform/lsf/8.0/x86-64-sol10/lib'],
                               extra_compile_args=['-m64'],			
                               extra_link_args=['-m64'],
                               libraries=['c', 'nsl', 'lsf', 'bat',
                                            'fairshareadjust', 'lsbstream'])],
      py_modules=['paltform-lsf.lsf'],
      classifiers=["Development Status :: 2 - Pre-Alpha",
                     "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Topic :: Internet",
                     "Topic :: Scientific/Engineering",
                     "Topic :: Software Development",
                     "Topic :: System :: Distributed Computing",
                     "Topic :: Utilities",
                     ],
     )

