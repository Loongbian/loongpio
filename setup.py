import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loongpio",
    version="0.0.1",
    author="Peter Zhang",
    author_email="boyue.zhang@pzhang.net",
    description="Loongson GPIO library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Loongbian/loongpio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)

