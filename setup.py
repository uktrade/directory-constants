"""
Export Directory constants
"""
from setuptools import setup, find_packages


setup(
    name='directory_constants',
    version='8.0.2',
    url='https://github.com/uktrade/directory-constants',
    license='MIT',
    author='Department for International Trade',
    description='Constant values shared between Directory apps.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=1.9,<2.0a1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
