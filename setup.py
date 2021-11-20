from distutils.core import setup
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
README = (here/"README.md").read_text()

setup(name='minisam_py',
      version='0.0.0',
      packages=['minisam_py', 'minisam_py.sophus'],
      license='MIT',
      description = 'Python wrapper for minisam and sophus with additional functionality.',
      author = 'Nikolaos Kourtzanidis',
      author_email = 'nkourtza@ryerson.ca',
      long_description=README,
      url = 'https://github.com/Nick-Kou/minisam_py.git',   # Provide either the link to your github or to your website
      download_url = 'https://github.com/Nick-Kou/minisam_py/archive/refs/tags/v0.0.0.tar.gz', 
      keywords = ['GRAPH OPTIMIZATION', 'SLAM', 'SOPHUS'],
      install_requires=['numpy','matplotlib',],
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",],
      package_dir={'minisam_py': 'here/minisam_py',
                   'minisam_py.sophus': 'here/minisam_py/sophus'},
      package_data={'minisam_py': ['here/minisam_py', 'libminisam*', 'minisam*'],
                    'minisam_py.sophus': ['here/minisam_py/sophus']})
     
