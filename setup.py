import sys
import json
from pathlib import Path
import setuptools
from setuptools.command.test import test as TestCommand

try:
    from importlib import resources
    install_requires = []
except:
    install_requires = ['importlib_resources']


name = 'reincarnation'

__version__ = None

here = Path(__file__).parent

# This should be replaced with proper pathlib business

exec((here / name / '_version.py').read_text())

description = (here / 'readme.md').read_text()


class PyTest(TestCommand):
    def run_tests(self):
        sys.exit(__import__('pytest').main([]))


setup_args = dict(
    name=name,
    version=__version__,
    author='deathbeds',
    author_email='tony.fast@gmail.com',
    description='JupyterCon 2018 presentation.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/deathbeds/'+name,
    python_requires='>=3.4',
    license='BSD-3-Clause',
    setup_requires=[
        'pytest-runner',
        'twine>=1.11.0',
        'setuptools>=38.6.',
    ] + ([] if sys.version_info.minor == 4 else ['wheel>=0.31.0']),
    tests_require=['pytest', 'nbformat'],
    install_requires=install_requires,
    include_package_data=True,
    packages=['reincarnation'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',),
    zip_safe=False,
    cmdclass={'test': PyTest},
)


if __name__ == '__main__':
    setuptools.setup(**setup_args)
