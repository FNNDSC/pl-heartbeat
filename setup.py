
import sys
import os

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()


setup(
      name             =   'heartbeat',
      # for best practices make this version the same as the VERSION class variable
      # defined in your main plugin app class
      version          =   '1.0.0',
      description      =   'A ChRIS app that periodically outputs system information',
      long_description =   readme(),
      author           =   'Arnav Nidumolu',
      author_email     =   'arnav.nidumolu@gmail.com',
      url              =   'https://github.com/FNNDSC/pl-heartbeat',
      packages         =   ['heartbeat'],
      install_requires =   ['chrisapp', 'pudb', 'psutil'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['heartbeat/heartbeat.py'],
      license          =   'MIT',
      zip_safe         =   False
     )