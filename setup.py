from setuptools import setup

setup(
    name='my_package',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/lucas-trubiano/my_package',
    author='Lucas Trubiano',
    author_email='lucas.trubiano@gmail.com',
    license='LICENSE',
    packages=['my_package'],
    install_requires=[
        # 'mpi4py>=2.0',
        # 'numpy',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: Other/Proprietary License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],

    # name='toolbox',
    # version='0.0.3',
    # author='Mike Huls',
    # author_email='mike_huls@hotmail.com',
    # description='Testing installation of Package',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url='https://github.com/mike-huls/toolbox',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    # license='MIT',
    # packages=['toolbox'],
    # install_requires=['requests'],


)