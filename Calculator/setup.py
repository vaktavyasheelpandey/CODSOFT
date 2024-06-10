from setuptools import setup, find_packages

setup(
    name="simple_calculator",
    version="0.1",
    packages=find_packages(),
    py_modules=["calculator"],
    entry_points={
        "console_scripts": [
            "calculator=calculator:main",
        ],
    },
    author="vaktavyasheelpandey",
    author_email="abhaypandey71833@gmail.com",
    description="A simple calculator that performs basic arithmetic operations.",
    long_description=open("README.md").read(),
)