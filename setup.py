from setuptools import setup, find_packages

setup(
    name='norskfaktura',
    version='0.0.1',
    description='Database solution for handling a small business',
    url='',
    author='Bjørnsen IT',
    author_email='bjornsenit@gmail.com',
    test_suite="nose.collector",
    tests_require=["nose"],
    license='MIT',
    entry_points = {
        "console_scripts" : [
            "fakturatest=norskfaktura.cmd:test",
        ],
    },
    packages=find_packages(include=['norskfaktura', 'norskfaktura.*']),
    include_package_data=True,
    install_requires=[
        "pycairo>=1.19.1",
        "PyGObject>=3.36.1",
        "reportlab>=3.5.44",
    ],
    zip_safe=False
)
