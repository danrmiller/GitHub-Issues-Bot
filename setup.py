from setuptools import setup, find_packages
 
 
with open('README.rst') as f:
    long_description = ''.join(f.readlines())
 
 
setup(
    name='issuelabeler',
    version='0.5',
    description='Labels unlabeled issues in GitHub repository.',
    long_description=long_description,
    author='Petr Klejch',
    author_email='klejcpet@fit.cvut.cz',
    keywords='github,issue,label',
    license='GPL-3.0',
    url='https://github.com/pklejch/GitHub-Issues-Bot',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
        ],
    install_requires=['Flask', 'click>=6', 'requests'],
    setup_requires=['pytest-runner','pytest'],
    tests_require=['pytest', 'betamax','configparser'],
    entry_points={
        'console_scripts': [
            'issuelabeler = issuelabeler.issuelabel:main',
        ],
    },
    package_data={
        'issuelabeler': ['static/*','templates/*','auth.conf.sample','rules.conf']
    },
    #include_package_data=True,
)
