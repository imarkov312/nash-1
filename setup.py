from setuptools import setup

setup(name='nash',
      version='0.1',
      description='Nash_equilibrium',
      url='https://github.com/smvlx/nash',
      author='Alexandr Smirnov',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['nash'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      zip_safe=False)