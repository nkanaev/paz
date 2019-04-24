from setuptools import setup, Command
from setuptools.command.test import test as TestCommand


def read(filename):
    return open(filename).read()


class PyTestCommand(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def run_tests(self):
        import sys, pytest
        sys.exit(pytest.main([]))


class PublishCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def info(self, s):
        print('\n\n', s, end='\n---\n', sep='')

    def run(self):
        import os, sys
        self.info('Building Source and Wheel (universal) distribution...')
        os.system('python3 setup.py sdist bdist_wheel')

        self.info('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')
        sys.exit()


setup(
    name='paz',
    version='0.0.1',
    description='simple path manipulation library',
    long_description=read('readme.rst'),
    author='Nazar Kanaev',
    author_email='nkanaev@live.com',
    url='https://github.com/nkanaev/paz',
    packages=['paz'],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={"test": PyTestCommand, 'publish': PublishCommand},
)
