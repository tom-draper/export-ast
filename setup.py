from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="export-ast",
    version="1.0.6",
    author="Tom Draper",
    author_email="tomjdraper1@gmail.com",
    license="MIT",
    description="Export a Python AST to a dictionary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tom-draper/ast-export",
    key_words="ast syntax trees export dict json dictionary",
    install_requires=[],
    packages=find_packages(),
    python_requires=">=3.6",
)