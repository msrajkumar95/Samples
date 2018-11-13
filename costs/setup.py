import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="costs",
    version="0.0.1",
    author="Rajkumar Srinivasan",
    author_email="msrajkumar95@gmail.com",
    description="A small package to create minimum cost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msrajkumar95/Samples",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)