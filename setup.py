from setuptools import setup

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
            
        ],
    },
    packages=['norskfaktura'],
    include_package_data=True,
    zip_safe=False
)
