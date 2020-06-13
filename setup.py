import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="parser-package-sms23uwf",
    version="0.0.1",
    author="Steven M. Satterfield",
    author_email="steve1@scholacity.org",
    description="an algorithm to parse a course catalog",
    long_description_content_type="text/markdown",
    url="https://github.com/sms23uwf/scholacity_parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    
)