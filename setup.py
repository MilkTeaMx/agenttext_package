"""Simple setup for local use"""

from setuptools import setup, find_packages

setup(
    name="agenttext",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests>=2.25.0"],
    python_requires=">=3.7",
)

