from setuptools import setup, find_packages
import os

DESCRIPTION = "Signal dispatcher for Python, extracted from the Django framework. Extended to support a 'capture all' signal named any_signal."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass


setup(name='pysignalsex',
      version='0.1.2',
      packages=find_packages(),
      author='Nick Zalutskiy',
      author_email='pacemkr@{nospam}gmail.com',
      url='https://github.com/pacemkr/PySignalsEx',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
)
