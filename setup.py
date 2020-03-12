from setuptools import setup

setup(name='alma_python_packages',
      version='1.4.3',
      description='Python module for making requests to the Alma API',
      url='https://github.com/JonkopingUniversityLibrary/almaapi',
      author='Gustav Lindqvist',
      author_email='gustav.lindqvist@ju.se',
      license='MIT',
      packages=[
            'alma_api',
            'alma_analytics_parser',
            'alma_marc'
      ],
      install_requires=[
            'httplib2',
            'xmljson',
      ],
      zip_safe=False)
