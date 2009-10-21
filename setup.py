import os
from setuptools import setup, find_packages

setup(
    name = "django-iscapetags",
    version = "0.1",
    author = "Mark Rogers",
    author_email = "markr@imagescape.com",
    url = "http://www.imagescape.com",
    
    packages = find_packages('.'),
    package_dir = {'':'.'},
    license = "BSD License",
    keywords = "django templatetags",
    description = "assortment of template tags",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python',
    ]
)
