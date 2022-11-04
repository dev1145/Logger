# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name='loggerdev',
 version='1.0',
 packages=['loggerdev'],
 license = 'MIT',
 description = 'get_logger',
 author = 'dev1145',
 author_email = '@gmail.com',
 keywords = ['logging','get_logger'],
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/dev1145/loggerdev",
 install_requires=[ 'psutil' ],
 include_package_data=True,
)
