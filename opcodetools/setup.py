import setuptools

# From the directory with this file
#   py setup.py sdist
#   py -m twine upload dist/*

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opcodetools",  # Replace with your own username
    version="1.0",
    author="Chris Cantrell",
    author_email="topherCantrell@gmail.com",
    description="Assemblers/Disassemblers for retro processors (Z80, 6502, 6809, etc)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/topherCantrell/computerarcheology",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
