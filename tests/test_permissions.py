from unittest.mock import patch
from paz import p


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
def test_chmod(os):
    p('test/file').chmod(0x777)
    os.chmod.assert_called_once_with('test/file', 0x777)


@patch('paz.os')
@patch('paz.pwd')
def test_owner(pwd, os):
    pwd.getpwuid().pw_name = 'admin'
    assert p('test/file').owner == 'admin'


@patch('paz.os')
@patch('paz.grp')
def test_group(grp, os):
    grp.getgrgid().gr_name = 'admin'
    assert p('test/file').group == 'admin'
