from unittest.mock import patch
from paz import p


@patch('paz.shutil')
def test_manipulation_copy(shutil):
    assert p('test/file').copy('{basepath}_backup') == 'test/file_backup'
    shutil.copy.assert_called_once_with('test/file', 'test/file_backup', follow_symlinks=True)


@patch('paz.shutil')
def test_manipulation_move(shutil):
    assert p('test/file').move('{basepath}_backup') == 'test/file_backup'
    shutil.move.assert_called_once_with('test/file', 'test/file_backup', copy_function=None)
