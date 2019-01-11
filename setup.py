"""
Export Directory constants
"""
from setuptools import setup, find_packages


setup(
    name='directory_constants',
    version='11.4.1',
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
    extras_require={
        'test': [
            'pytest==3.0.2',
            'pytest-cov==2.3.1',
            'pytest-django==3.0.0',
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
