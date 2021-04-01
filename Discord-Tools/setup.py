from setuptools import setup, find_packages
import os



VERSION = '6.1'
DESCRIPTION = 'Simulates Discord User'

# Setting up
setup(
    name="Discord_Tools",
    version=VERSION,
    author="TanmayArya1-p",
    author_email="<tanmayarya2018@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium', 'beautifulsoup4','pyttsx3','speechrecognition'],
    keywords=['python', 'selenium', 'web-scraping', 'discord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)