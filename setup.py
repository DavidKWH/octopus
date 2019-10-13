from setuptools import setup, find_packages
#import numpy

setup(name='octopus',
      version='0.1.0',
      packages=find_packages(),
      #package_data={'': ['*.txt']},
      #scripts=['bin/rclone.py'],
      #install_requires=["numpy",
      #                  "Cython",
      #                  "importlib_resources ; python_version<'3.7'"],
      #include_dirs=[numpy.get_include()],
      #license='LICENSE.txt',
      description='Task queue for hetergenenous network nodes'
      #long_description=open('README.txt').read(),
      #url='http://pypi.python.org/pypi/CommLib/',
      author='David K. W. Ho',
      author_email='davidkwho@gmail.com',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
      ],
      )
