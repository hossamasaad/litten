from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'A python package to visualize sequentail tensorflow model archtictures'

# Setting up
setup(
    name="litten",
    version=VERSION,
    author="Hossam Asaad",
    author_email="hossamasaad10@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,  
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'tensorflow', 'keras', 'PIL', 'pillow', 'visualize models', 'visualize'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'Pillow>=9.3.0',
    ],
    python_requires='>=3.6',
)