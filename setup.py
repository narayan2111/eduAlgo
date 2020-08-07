from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Education',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    ]

# calling the setup function
setup(name='eduAlgo',
      version='1.0.1',
      description='An educational Algorithmic Library',
      long_description=long_description,
      url='https://github.com/Abhijit2505/eduAlgo',
      author='Abhijit Tripathy',
      author_email='abhijittripathy99@gmail.com',
      license='MIT',
      packages=['edualgo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='algorithms'
      )