from setuptools import setup

import encipher

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pg-encipher",
    author=encipher.__author__,
    author_email=encipher.__email__,
    version=encipher.__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=encipher.__github__,
    packages=["pg_encipher"],
    entry_points={"console_scripts": ["encipher=encipher.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    exclude=("__pycache__",),
)