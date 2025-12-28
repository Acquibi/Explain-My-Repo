# setup.py
from setuptools import setup, find_packages

setup(
    name="explain-my-repo",
    version="0.1.0",
    description="Analyze a repository and generate a summary and a diagram.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "gitpython>=3.1.31",
        "graphviz>=0.20.1",
        "openai>=0.27.0",
        "rich>=13.3.2",
        "click>=8.1.7",
    ],
    entry_points={
        "console_scripts": [
            "explain_repo=explain_my_repo.cli:main",
        ]
    },
)
