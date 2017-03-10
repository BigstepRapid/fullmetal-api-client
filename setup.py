from distutils.core import setup

from setuptools import find_packages

version = '0.1'
name = 'fullmetal-api-client'
url = 'https://github.com/adiciausu/fullmetal-api-client-python'

setup(
    name=name,
    packages=find_packages(),
    version=version,
    description='Api client for FullMetal infrastucture',
    author='Bigstep inc',
    author_email='adrian.ciausu@bigstep.com',
    url=url,
    download_url=url + 'tarball/' + version,
    keywords=['fullmetal', 'infrastructure', 'api', 'client'],
    classifiers=[]
)
