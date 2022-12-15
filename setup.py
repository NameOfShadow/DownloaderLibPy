from setuptools import setup
with open("README.md", encoding="utf-8") as file:
	long_description=file.read()
setup(
	name='downloaderlib',
    version='3.2',
    description='This library is for downloading picture, GitHub files, audio and etc.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['downloaderlib'],
   author_email='0nameofshadow0@gmail.com',
    install_requires=["mureq"])