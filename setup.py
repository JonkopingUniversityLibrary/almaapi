from setuptools import setup

setup(name='almaapi',
      version='1.2',
      description='Python module for making requests to the Alma API',
      url='https://github.com/JonkopingUniversityLibrary/almaapi',
      author='Gustav Lindqvist',
      author_email='gustav.lindqvist@ju.se',
      license='MIT',
      packages=['almaapi', 'almamarc'],
      install_requires=[
            'httplib2'
      ],
      zip_safe=False)
