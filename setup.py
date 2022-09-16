from setuptools import setup

setup(
    name='statsmodels',
    version='1.0.0',
    description='A ChRIS plugin to perform statsmodels operations',
    author='FNNDSC',
    author_email='dbassey@redhat.com',
    url='https://github.com/rh-impact/pl-statsmodels',
    py_modules=['statsmodels'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'statsmodels = statsmodels:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
