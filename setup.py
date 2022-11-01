from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bala_lib_management/__init__.py
from bala_lib_management import __version__ as version

setup(
	name="bala_lib_management",
	version=version,
	description="lib manager",
	author="Nxweb",
	author_email="info@nxweb.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
