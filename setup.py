# Import required functions
from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Call setup function
setup(
    author="Javad Ebadi",
    author_email="javad.ebadi.1990@gmail.com",
    description="A simple python library for bookkeeping",
    name="pybookkeeping",
    packages=find_packages(include=["pybookkeeping", "pybookkeeping.*"]),
    version="0.0.0",
    install_requires=[],
    python_requires='>=3.6',
    license='MIT',
    url='https://github.com/javadebadi/pybookkeeping',
    long_description=long_description,
    long_description_content_type='text/markdown'
)