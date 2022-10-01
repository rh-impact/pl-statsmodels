from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), "README.rst")) as f:
    readme = f.read()

setup(
    name="pl_statsmodels",
    version="0.1",
    description="Fits OLS model to given data",
    long_description=readme,
    author="apal",
    author_email="apal@redhat.com",
    url="https://github.com/rh-impact/pl-statsmodels/blob/main/README.adoc'",
    packages=["pl_statsmodels"],
    install_requires=["chrisapp"],
    test_suite="nose.collector",
    tests_require=["nose"],
    license="MIT",
    zip_safe=False,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["pl_statsmodels = pl_statsmodels.__main__:main"]},
)
