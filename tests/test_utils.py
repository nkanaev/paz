import inspect
from unittest.mock import patch
from paz import p, pazmixin


@patch('paz.open', create=True)
def test_hash(open):
    open().__enter__().read.return_value = b'hello world'
    assert p('test/file').hash('md5') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert p('test/file').hash('sha256') == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'


@patch('paz.os')
def test_chdir(os):
    p('test/dir').chdir()
    os.chdir.assert_called_once_with('test/dir')


@patch('paz.open', create=True)
def test_open(open):
    assert p('test/file').open('rb') == open.return_value
    open.assert_called_once_with('test/file', 'rb')


def test_api():
    is_method_or_property = lambda x: inspect.isfunction(x) or inspect.isdatadescriptor(x)

    for klass in (str, bytes):
        for attr, _ in inspect.getmembers(pazmixin, predicate=is_method_or_property):
            if attr.startswith('__'):
                continue
            assert not hasattr(klass, attr), '"%s" is overriden for %s' % (attr, klass)
