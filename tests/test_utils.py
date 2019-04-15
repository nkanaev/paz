from unittest.mock import patch
from paz import p


@patch('paz.open')
def test_hash(open):
    open().__enter__().read.return_value = b'hello world'
    assert p('test/file').hash('md5') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert p('test/file').hash('sha256') == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
