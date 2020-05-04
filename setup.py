from setuptools import setup, find_packages

setup(
    name="minimal-deploy",
    description='A minimal Python package',
    author='Talley',
    author_email='talley.lambert@gmail.com',
    url='https://github.com/tlambert03/minimal-deploy',
    packages=find_packages(),
    use_scm_version={"write_to": "minimal/_version.py"},
    setup_requires=['setuptools_scm'],
)