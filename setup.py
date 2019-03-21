from setuptools import setup

setup(name='almaapi',
      version='0.1',
      description='Python module for making requests to the Alma API',
      url='https://github.com/JonkopingUniversityLibrary/almaapi',
      author='Gustav Lindqvist',
      author_email='gustav.lindqvist@ju.se',
      license='MIT',
      packages=['almaapi'],
      install_requires=[
            'httplib2'
      ],
      zip_safe=False)
