import codecs
from setuptools import setup


def read(filename):
    return codecs.open(filename, encoding='utf8').read()


setup(
    name='paz',
    version='0.0.1',
    description='simple path manipulation library',
    long_description=read('readme.rst'),
    author='Nazar Kanaev',
    author_email='nkanaev@live.com',
    url='https://github.com/nkanaev/paz',
    py_modules=['paz'],
    #package_data={'': ['LICENSE']},
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
)
