from setuptools import setup, find_packages
import kruxpy

setup(
    name="kruxpy",
    version=kruxpy.__version__,
    description="Kruxpy is a library for dealing with the Krux / Salesforce DMP API",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/theatlantic/kruxpy",
    packages=find_packages(),
    python_requires='>=3',
    install_requires=["requests==2.20.0"]
)
