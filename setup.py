import codecs
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(filename):
    return codecs.open(filename, encoding='utf8').read()


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex, sys, pytest
        sys.exit(pytest.main(shlex.split(self.pytest_args)))


setup(
    name='paz',
    version='0.0.1',
    description='simple path manipulation library',
    long_description=read('readme.rst'),
    author='Nazar Kanaev',
    author_email='nkanaev@live.com',
    url='https://github.com/nkanaev/paz',
    py_modules=['paz'],
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
    cmdclass={"test": PyTest},
)
