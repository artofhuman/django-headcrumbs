from setuptools import setup, find_packages

setup(
    name = 'django-headcrumbs',
    version = '0.1.0',
    description = 'Smart and easy-to-use breadcrumbs for Django',
    url = 'https://github.com/kirelagin/django-headcrumbs',
    license = 'MIT',
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 2.7',
        'Programming Language :: Python 3.0',
        'Programming Language :: Python 3.1',
        'Programming Language :: Python 3.2',
        'Programming Language :: Python 3.3',
    )
)
