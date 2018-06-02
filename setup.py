from setuptools import setup, find_packages

setup(
    name='dukedoms-card-service-mock-tests',
    version='0.0.0',
    description='containerized tests for dukedoms card service mock',
    packages=find_packages(exclude=['&.tests']),
    install_requires=[
        'addict',
        'behave',
        'bravado',
        'pyhamcrest'
    ]
)
