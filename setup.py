import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_canalyzer", # Replace with your own username
    version="0.0.2",
    author="Guopeng Sun",
    author_email="sgnes0514@gmai.com",
    description="Vector CANalyzer Win32Com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgnes/PythonCanalyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pywin32',
          'pypiwin32',
      ],
    python_requires='>=3.6',
)