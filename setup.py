"""
Flask-MinioClient
-------------

This is the description for that library
"""
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-MinioClient',
    version='1.0',
    url='https://github.com/haojunyu/flask-minioclient',
    license='MIT',
    author='haojunyu',
    author_email='haojunyu2012@gmail.com',
    description='Minio Client extension for Flask',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_minioclient'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'minio',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
