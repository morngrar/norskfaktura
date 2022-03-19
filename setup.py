from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='norskfaktura',
    version='0.1.8',
    description='Norwegian database solution for invoicing in a small business',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='',
    author='Svein-Kåre Bjørnsen',
    author_email='bjornsenit@gmail.com',
    test_suite="nose.collector",
    tests_require=["nose"],
    license='GPL-3.0-only',
    entry_points = {
        "console_scripts" : [
            "nf-dev=norskfaktura.cmd:dev",
            "nf-install-icons=norskfaktura.cmd:install_icons",
            "norskfaktura=norskfaktura.cmd:main",
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
