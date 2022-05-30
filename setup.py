import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="submission",
    version="0.0.0b0",
    author="Jacob Kravits",
    author_email="kravitsjacob@gmail.com",
    description="Submission for NSF CAREER commpetition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "submission"},
    packages=setuptools.find_packages(where="submission"),
    python_requires=">=3.7",
)
