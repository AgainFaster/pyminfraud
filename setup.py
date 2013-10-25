import setuptools
import pyminfraud

setuptools.setup(
	name=pyminfraud.__project__,
	version=pyminfraud.__version__,
	author=pyminfraud.__author__,
	author_email=pyminfraud.__email__,
	license=pyminfraud.__license__,

	description = 'Python library for interfacing with MaxMind\'s minFraud Web Service API.',
	keywords = 'python maxmind minfraud',
	packages = setuptools.find_packages(),
	maintainer = 'Joshua D. Burns',
	url = 'https://github.com/JDBurnZ/pyminfraud',
)
