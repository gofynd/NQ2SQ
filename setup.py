from setuptools import setup

setup(name='NQ2SQ',
      version='0.1',
      description='Tool to convert natural language questions as input and query.',
      url='https://gitlab.com/fynd/NQ2SQ',
      author='Siva subramani',
      author_email='sivasubramani@gofynd.com',
      license='MIT',
      packages=['NQ2SQ'],
      zip_safe=False,
      install_requires=['click', 'nltk'])
