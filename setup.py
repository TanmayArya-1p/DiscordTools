from setuptools import setup, find_packages
import os



VERSION = '1.3'
DESCRIPTION = 'Navigating through Discord Programatically using Selenium Webscraping(using Chrome Webdriver)'

# Setting up
setup(
    name="Discord_Tools",
    version=VERSION,
    author="TanmayArya1-p",
    author_email="<tanmayarya2018@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium'],
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