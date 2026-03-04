"""
Setup script for lema001

This is a legacy setup.py for compatibility with older tools.
The primary configuration is in pyproject.toml
"""

from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lema001",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="实验项目库 - 所有的实验项目都以 lema 打头后面加序号，这个是第一个项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/lema001",
    packages=find_packages(where="."),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        # 在这里添加你的项目依赖
        # 例如：requests>=2.28.0
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "lema001=lema001:main",
        ],
    },
)
