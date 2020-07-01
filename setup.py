from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./tests')

from src import __TITLE__, __VERSION__

setup(
        name = __TITLE__,
        version = __VERSION__,
        description = "A story build package",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
