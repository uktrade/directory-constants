"""
Export Directory constants
"""
from setuptools import setup, find_packages


setup(
    name='directory_constants',
    version='20.28.0',
    url='https://github.com/uktrade/directory-constants',
    license='MIT',
    author='Department for International Trade',
    description='Constant values shared between Directory apps.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_data={
        'directory_constants': [
            'fixtures/*',
            'locale/*',
        ]
    },
    include_package_data=True,
    install_requires=[
        'django>=1.11,<=3.1.7',
    ],
    extras_require={
        'test': [
            'pytest==3.6.0',
            'pytest-cov==2.7.1',
            'pytest-django==3.3.0',
            'flake8==3.0.4',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'freezegun==0.3.8',
            'setuptools>=38.6.0,<39.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
