from unittest.mock import patch
from datetime import datetime
from paz import p


@patch('paz.os')
def test_predicates(os):
    assert p('test/path1').is_dir == os.path.isdir.return_value
    assert p('test/path2').is_file == os.path.isfile.return_value
    assert p('test/path3').is_link == os.path.islink.return_value
    assert p('test/path4').exists == os.path.exists.return_value

    os.path.isdir.assert_called_once_with('test/path1')
    os.path.isfile.assert_called_once_with('test/path2')
    os.path.islink.assert_called_once_with('test/path3')
    os.path.exists.assert_called_once_with('test/path4')


@patch('paz.os')
def test_times(os):
    now = datetime.now()
    os.path.getmtime.return_value = now.timestamp()
    os.path.getatime.return_value = now.timestamp()

    assert p('test/path').last_accessed == now
    assert p('test/path').last_modified == now
