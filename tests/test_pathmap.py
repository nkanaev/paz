from paz import p

import pytest


def test_pathmap():
    # absolute paths
    assert p('/path/to/file.txt').pathmap('{path}') == '/path/to/file.txt'
    assert p('/path/to/file.txt').pathmap('{basepath}') == '/path/to/file'
    assert p('/path/to/file.txt').pathmap('{filename}') == 'file.txt'
    assert p('/path/to/file.txt').pathmap('{basename}') == 'file'
    assert p('/path/to/file.txt').pathmap('{dirname}') == '/path/to'
    assert p('/path/to/file.txt').pathmap('{ext}') == 'txt'

    # relative paths
    assert p('dir/file.txt').pathmap('{path}') == 'dir/file.txt'
    assert p('dir/file.txt').pathmap('{path}') == 'dir/file.txt'
    assert p('dir/file.txt').pathmap('{basepath}') == 'dir/file'
    assert p('dir/file.txt').pathmap('{filename}') == 'file.txt'
    assert p('dir/file.txt').pathmap('{basename}') == 'file'
    assert p('dir/file.txt').pathmap('{dirname}') == 'dir'
    assert p('dir/file.txt').pathmap('{ext}') == 'txt'

    # filenames
    assert p('file.txt').pathmap('{path}') == 'file.txt'
    assert p('file.txt').pathmap('{basepath}') == 'file'
    assert p('file.txt').pathmap('{filename}') == 'file.txt'
    assert p('file.txt').pathmap('{basename}') == 'file'
    assert p('file.txt').pathmap('{dirname}') == ''
    assert p('file.txt').pathmap('{ext}') == 'txt'


def test_pathmap_advanced():
    assert p('/path/to/file.txt').pathmap('{basepath}_backup.{ext}') == '/path/to/file_backup.txt'


def test_pathmap_exception():
    with pytest.raises(ValueError, match='extension'):
        p('/path/to/file.txt').pathmap('{basename}.{extension}')
