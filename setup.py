from setuptools import setup

import cipher

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pg-cipher",
    author=cipher.__author__,
    author_email=cipher.__email__,
    version=cipher.__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=cipher.__github__,
    packages=["cipher"],
    entry_points={"console_scripts": ["cipher=cipher.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires="<=3.8",
    include_package_data=True,
    exclude=("__pycache__",),
)