import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Color_Console",
    version="1.0.0",
    author="Sayad Pervez",
    author_email="pervez2504@gmail.com",
    description="Comprehensive Utility Library for changing the color of text and background of a python console.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SayadPervez/Color_Console",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
