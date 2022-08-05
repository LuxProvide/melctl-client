from setuptools import setup, find_packages

from melctl_client import __version__


setup(
  name='melctl_client',
  author='@jpclipffel',
  url='https://gitlab.lxp.lu/lxp-hpc/iac/meluxina/melctl-client',
  version=__version__,
  packages=find_packages('.'),
  entry_points={
    'console_scripts': [
      'melctl-client=melctl_client.__main__:main',
      'melctl=melctl_client.__main__:main'
    ]
  },
  install_requires=[
      'requests',
      'tabulate',
      'pygments',
      'pydantic[dotenv]',
      'pyyaml',
      'python-jose[cryptography]',
  ]
)
