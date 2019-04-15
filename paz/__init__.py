import os
import re
import shutil
import stat
import pwd
import grp


__version__ = '0.0.1'


class p(str):
    @property
    def exists(self):
        return os.path.exists(self)

    @property
    def is_dir(self):
        return os.path.isdir(self)

    @property
    def is_file(self):
        return os.path.isfile(self)

    @property
    def is_link(self):
        return os.path.islink(self)

    @property
    def fullpath(self):
        return p(os.path.abspath(os.path.expanduser(self)))

    @property
    def path(self):
        return self

    @property
    def basepath(self):
        return os.path.join(self.dirname, self.basename)

    @property
    def dirname(self):
        return os.path.dirname(self)

    @property
    def basename(self):
        return os.path.splitext(os.path.basename(self))[0]

    @property
    def filename(self):
        return os.path.basename(self)

    @property
    def ext(self):
        return os.path.splitext(self)[1][1:]

    def pathmap(self, pattern):
        newpath = ''
        for part in re.split(r'({\w+})', pattern):
            if part.startswith('{') and part.endswith('}'):
                part = part[1:-1]
                if not hasattr(self, part):
                    raise ValueError('unknown pathmap specifier "{}" in "{}"'.format(part, pattern))
                newpath += getattr(self, part)
            else:
                newpath += part
        return p(newpath)

    def __truediv__(self, other):
        return p(os.path.join(self, other))

    def __rtruediv__(self, other):
        return p(os.path.join(other, self))

    def copy(self, pattern, copy_metadata=False, follow_symlinks=True):
        newp = self.pathmap(pattern)
        copyfn = shutil.copy if not copy_metadata else shutil.copy2
        copyfn(self, newp, follow_symlinks=follow_symlinks)
        return newp

    def move(self, pattern, copy_function=None):
        newp = self.pathmap(pattern)
        shutil.move(self, newp, copy_function=copy_function)
        return newp

    def open(self, *args, **kwargs):
        return open(self, *args, **kwargs)

    def chdir(self):
        # TODO: context processor
        os.chdir(self)

    def chown(self, owner=None, group=None):
        if not owner and not group:
            raise Exception('provide either "owner" or "group"')
        uid, gid = owner, group
        if isinstance(uid, str):
            uid = pwd.getpwuid(uid).pw_uid
        if isinstance(gid, str):
            gid = grp.getgrnam(gid).gr_gid
        return os.chown(self, uid, gid)

    def __repr__(self):
        return 'p({})'.format(super().__repr__())
