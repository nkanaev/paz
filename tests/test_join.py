from paz import p


def test_join():
    assert p('test/dir') / 'subdir' == 'test/dir/subdir'
    assert 'parent' / p('test/dir') == 'parent/test/dir'
