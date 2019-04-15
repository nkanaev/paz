from unittest.mock import patch
from paz import p


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
