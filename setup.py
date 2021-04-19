from setuptools import setup, find_packages
import os



VERSION = '2.1'
DESCRIPTION = 'Simulates Discord User using Selenium(Web-Scraping) Chromium-webdriver'

# Setting up
setup(
    name="Discord_Tools",
    version=VERSION,
    author="TanmayArya1-p",
    author_email="<tanmayarya2018@gmail.com>",
    description=DESCRIPTION,
    url='https://github.com/TanmayArya-1p/DiscordTools',
    install_requires=['selenium', 'beautifulsoup4','pyttsx3','speechrecognition'],
    keywords=['python', 'selenium', 'web-scraping', 'discord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)