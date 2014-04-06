from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-secretballot',
    version="0.2.5",
    package_dir={'secretballot': 'secretballot'},
    packages=['secretballot'],
    description='Django anonymous voting application',
    author='James Turk, Niklas Plessing',
    author_email='jturk@sunlightfoundation.com, contact@niklasplessing.net',
    license='BSD License',
    url='https://github.com/niklasp/django-secretballot',
    long_description=long_description,
    platforms=["any"],
    install_requires=[
        "django",
        "south",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
