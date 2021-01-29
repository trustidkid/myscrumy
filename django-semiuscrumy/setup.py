import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


#allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-semiuscrumy',  # Replace with your own username
    version='0.1',
    author='Semiu Biliaminur',
    author_email='yemi.bili07@gmail.com',
    description='A simple application',
    license = 'BSD License',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/trustidkid/myscrumy',
    packages=find_packages(),
    include_package_data=True,
    
    classifiers=[
        'Environment :: Web Environemnt',
        'Framework :: Django',
        'Framework :: Django :: '
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6.8',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intendend Audience :: Developer',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'

    ]
)
