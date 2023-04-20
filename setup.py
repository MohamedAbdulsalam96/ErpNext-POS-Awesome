from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in posawesome_free/__init__.py
from posawesome_free import __version__ as version

setup(
	name="posawesome_free",
	version=version,
	description="POSAWESOME FREE",
	author="Sagar Ratan Garg",
	author_email="sagar1ratan1garg1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
