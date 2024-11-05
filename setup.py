from setuptools import setup, find_packages
__project__ = 'Mmath_quiz'
__description__ = 'Simple Math Quiz Game'
__package__ = find_packages()
__version__ = '62.51'
__author__ = 'Abdur Razzak'
__email__ = 'abdur.razzak@fau.de'
__classifiers__ = ['Development Status :: 1 - Planning',
                    'Intended Audience :: Education',
                    'Programming Language :: Python',
                    'Operating System :: OS Independent',]
__requires__ = []

setup(name = __project__,
      version = __version__,
      description = __description__,
      author = __author__,
      author_email = __email__,
      packages = __package__,
      classifiers=__classifiers__,
      requires=__requires__,
      # url =
      )
