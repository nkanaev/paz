from setuptools import setup, Command
from setuptools.command.test import test as TestCommand


class PyTestCommand(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def run_tests(self):
        import sys, pytest
        sys.exit(pytest.main([]))


setup(
    name='paz',
    version='0.0.1',
    description='path manipulation swiss army knife',
    long_description=open('readme.rst').read(),
    author='Nazar Kanaev',
    author_email='nkanaev@live.com',
    url='https://github.com/nkanaev/paz',
    packages=['paz'],
    package_data={'': ['readme.rst']},
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
    cmdclass={"test": PyTestCommand},
)
