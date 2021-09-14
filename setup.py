import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [

]

setuptools.setup(
    name="modelstat",
    version="0.0.1",
    author="Chilin",
    author_email="chilin.cs07@nycu.edu.tw",
    description="modelstat is CLI tool to summarize the Machine Learning model layer inference time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chilin0525/model-layer-profiling/tree/pypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'modelstat=src.main:main',
        ],
    },
    install_requires=install_requires,
    python_requires='>=3.8',
)
