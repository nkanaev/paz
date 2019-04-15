from unittest.mock import patch
from paz import p


@patch('paz.open')
def test_open(open):
    assert p('test/file').open('rb') == open.return_value
    open.assert_called_once_with('test/file', 'rb')


@patch('paz.grp')
@patch('paz.pwd')
@patch('paz.os')
def test_chown(os, pwd, grp):
    pwd.getpwuid().pw_uid = 10
    grp.getgrnam().gr_gid = 20
    assert p('test/file').chown('admin', 'www-data') == os.chown.return_value
    os.chown.assert_called_once_with('test/file', 10, 20)
    os.chown.reset_mock()

    assert p('test/file').chown(30, 40) == os.chown.return_value
    os.chown.assert_called_once_with('test/file', 30, 40)


@patch('paz.os')
def test_chdir(os):
    p('test/dir').chdir()
    os.chdir.assert_called_once_with('test/dir')


@patch('paz.shutil')
def test_manipulation_copy(shutil):
    assert p('test/file').copy('{basepath}_backup') == 'test/file_backup'
    shutil.copy.assert_called_once_with('test/file', 'test/file_backup', follow_symlinks=True)


@patch('paz.shutil')
def test_manipulation_move(shutil):
    assert p('test/file').move('{basepath}_backup') == 'test/file_backup'
    shutil.move.assert_called_once_with('test/file', 'test/file_backup', copy_function=None)
