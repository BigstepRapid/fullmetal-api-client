from distutils.core import setup
from setuptools import find_packages

version = '2.10'
name = 'metalcloud-api-client'
url = 'https://github.com/bigstepinc/metalcloud-api-client-python'

setup(
    name=name,
    packages=find_packages(),
    version=version,
    description='Api client for Metal Cloud infrastructure',
    author='Bigstep Inc.',
    author_email='bsiteam@bigstep.com',
    url=url,
    download_url= url + '/tarball/' + version,
    keywords=["metal", "cloud", "api", "client"],
    install_requires = [ 'jsonrpc2-base==0.7' ],
    classifiers=[]
)
