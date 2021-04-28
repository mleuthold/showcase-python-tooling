from setuptools import setup

setup(name='marleu-emr',
      version='0.1',
      description='Deployment tools for EMR',
      url='https://github.com/mleuthold/python-tooling',
      author='Martin Leuthold',
      author_email='martinleuthold88+github@gmail.com',
      license='MIT',
      packages=['marleu_emr'],
      install_requires=[
          'requests',
          'paramiko',
          'credstash',
          'cryptography==3.3.2'
      ],
      scripts=['bin/marleu-emr'],
      zip_safe=False)