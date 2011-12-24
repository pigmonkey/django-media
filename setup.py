from setuptools import setup, find_packages

setup(
    name = 'django-media',
    version = '0.1',
    description = 'A basic Django application to store and manage media.',
    long_description = open('README.md').read(),
    url = 'https://github.com/pigmonkey/django-media',
    author = 'Pig Monkey',
    author_email = 'pm@pig-monkey.com',

    packages = find_packages(),
    zip_safe=False,
)
