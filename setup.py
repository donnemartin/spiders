from setuptools import setup, find_packages

setup(
    name='spiders',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'scrapy>=1.0.3',
    ],
    entry_points={'scrapy': ['settings = spiders.settings']},
)
