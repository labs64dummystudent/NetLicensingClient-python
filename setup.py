import setuptools

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
setuptools.setup(name='netlicensing-python-client',
                 version='0.0.1.dev2',
                 description='Python wrapper for Labs64 NetLicensing RESTful API',
                 long_description=open('README.md').read().strip(),
                 long_description_content_type="text/markdown",
                 author='Labs64 NetLicensing',
                 author_email='info@netlicensing.io',
                 url='https://github.com/Labs64/NetLicensingClient-python',
                 project_urls={
                     'NetLicensing': 'https://netlicensing.io',
                     'Documentation': 'https://netlicensing.io/documentation/',
                     'Source': 'https://github.com/Labs64/NetLicensingClient-python',
                     'Tracker': 'https://github.com/Labs64/NetLicensingClient-python/issues',
                 },
                 py_modules=['netlicensing'],
                 install_requires=[],
                 license='Apache-2.0',
                 zip_safe=False,
                 keywords='labs64 netlicensing licensing licensing-as-a-service license license-management software-license client restful restful-api python wrapper api client',
                 classifiers=[
                     # https://pypi.org/classifiers/
                     'Development Status :: 1 - Planning',
                     'Environment :: Other Environment',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Information Technology',
                     'License :: OSI Approved :: Apache Software License',
                     'Natural Language :: English',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                     'Topic :: System :: Software Distribution',
                     'Topic :: Utilities'
                 ],
                 python_requires='>=3.6',
                 )
