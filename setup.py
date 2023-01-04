from setuptools import setup, find_packages, find_namespace_packages

from melctl_client import __version__


setup(
    name='melctl_client',
    author='@jpclipffel',
    url='https://gitlab.lxp.lu/lxp-hpc/iac/meluxina/melctl-client',
    version=__version__,
    packages=find_packages('.') + find_namespace_packages(include=['melctl_client_plugins.*']),
    entry_points={
        'console_scripts': [
            'melctl-client=melctl_client.__main__:main',
            'melctl=melctl_client.__main__:main'
        ]
    },
    install_requires=[
        'requests >= 1.28',
        'tabulate >= 0.8',
        'pygments >= 2.12',
        'pydantic[dotenv] >= 1.9',
        'pyyaml >= 6.0',
        'python-jose[cryptography] >= 3.3',
        # Library stubs
        'types-pyyaml',
        'types-tabulate',
        'types-pygments'
    ]
)
