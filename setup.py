from setuptools import setup, find_packages

setup(
    name = 'django-media',
    packages = find_packages(),
    version = '1.0',
    description = 'A basic Django application to store and manage media.',
    author = 'Peter Hogg',
    author_email = 'peter@havenaut.net',
    url = 'https://github.com/pigmonkey/django-media',
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
    ],
    long_description = open('README.md').read(),
    include_package_data = True,
    zip_safe=False,
    install_requires = ['PIL'],
)
