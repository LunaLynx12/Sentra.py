from setuptools import setup, find_packages

setup(
    name='sentra-api',
    version='0.1.0',
    author='LunaLynx12',
    author_email='lynalynx@example.com',
    description='A Python client for interacting with the Sentra API',
    url='https://github.com/LunaLynx12/Hackathon ',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)