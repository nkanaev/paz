# coding: utf-8
import os
import re
import shutil
import stat
import pwd
import grp
import hashlib
import datetime
import fnmatch


__version__ = '0.0.1'


FILE_PARTS = {'dirname', 'basename', 'ext', 'filename', 'basepath', 'path'}

FILE_TYPES = {
    stat.S_IFBLK: "blockdev",
    stat.S_IFCHR: "chardev",
    stat.S_IFDIR: "dir",
    stat.S_IFIFO: "fifo",
    stat.S_IFLNK: "link",
    stat.S_IFREG: "file",
    stat.S_IFSOCK: "socket",
}


class p(str):
    @property
    def owner(self):
        """Path owner string."""
        return pwd.getpwuid(os.lstat(self).st_uid).pw_name

    @property
    def group(self):
        """Path group string."""
        return grp.getgrgid(os.lstat(self).st_gid).gr_name

    @property
    def last_accessed(self):
        """File's last accessed date."""
        return datetime.datetime.fromtimestamp(os.path.getatime(self))

    @property
    def last_modified(self):
        """File's last modified date."""
        return datetime.datetime.fromtimestamp(os.path.getmtime(self))

    @property
    def exists(self):
        """True if path exists."""
        return os.path.exists(self)

    @property
    def is_dir(self):
        """True if path is a directory."""
        return os.path.isdir(self)

    @property
    def is_file(self):
        """True if path is a regular file."""
        return os.path.isfile(self)

    @property
    def is_link(self):
        """True if path is a symbolic link."""
        return os.path.islink(self)

    @property
    def type(self):
        """Returns readable file type. Can be one of the following below:
        'blockdev' / 'chardev' / 'dir' / 'fifo' / 'link' / 'file' / 'socket' / 'unknown'
        """
        return FILE_TYPES.get(stat.S_IFMT(os.lstat(self).st_mode), 'unknown')

    @property
    def fullpath(self):
        """Returns absolute path, expanding user."""
        return p(os.path.abspath(os.path.expanduser(self)))

    @property
    def path(self):
        """Full path."""
        return self

    @property
    def basepath(self):
        """Full path without extension."""
        return os.path.join(self.dirname, self.basename)

    @property
    def dirname(self):
        """The directory of the path."""
        return os.path.dirname(self)

    @property
    def basename(self):
        """The file name, without extension."""
        return os.path.splitext(os.path.basename(self))[0]

    @property
    def filename(self):
        """The file name of the path."""
        return os.path.basename(self)

    @property
    def ext(self):
        """File extension"""
        return os.path.splitext(self)[1][1:]

    def pathmap(self, pattern):
        """Returns a new path by substituting curly brace delimited path parts in a pattern.
        The supported path parts are illustrated below:

        /home/username/pics/portrait-of-madame-x.png

        └────────┬────────┘ └─────────┬────────┘ └┬┘
              dirname              basename      ext
                            └───────────┬──────────┘
                                    filename
        └───────────────────┬──────────────────┘
                        basepath
        └──────────────────────┬───────────────────┘
                             path
        """
        newpath = ''
        for part in re.split(r'({\w+})', pattern):
            if part.startswith('{') and part.endswith('}'):
                part = part[1:-1]
                if part not in FILE_PARTS:
                    raise ValueError('unknown pathmap specifier "{}" in "{}"'.format(part, pattern))
                newpath += getattr(self, part)
            else:
                newpath += part
        return p(newpath)

    def hash(self, name):
        """Hash string of the file using the provided hash algorithm."""
        hasher = getattr(hashlib, name)()
        with self.open('rb') as f:
            hasher.update(f.read())
            return hasher.hexdigest()

    def find(self, include=None, exclude=None, type=None):
        """Returns a generator which recursively descends the directory tree
        yielding matching paths.
        """
        for root, dirs, files in os.walk(self):
            for sub in [dirs, files]:
                for n in sub:
                    newp = p(os.path.join(root, n))
                    if include and not fnmatch.fnmatch(newp, include):
                        continue
                    if exclude and fnmatch.fnmatch(newp, exclude):
                        continue
                    if type and newp.type != type:
                        continue
                    yield newp

    def __truediv__(self, other):
        """Join path with another path/string."""
        return p(os.path.join(self, other))

    def __rtruediv__(self, other):
        """Left join path with another path/string."""
        return p(os.path.join(other, self))

    def copy(self, pattern, copy_metadata=False, follow_symlinks=True):
        """Copies file to a new target.
        Target string is substituted according to ``pathmap`` rules.
        """
        newp = self.pathmap(pattern)
        copyfn = shutil.copy if not copy_metadata else shutil.copy2
        copyfn(self, newp, follow_symlinks=follow_symlinks)
        return newp

    def move(self, pattern, copy_function=None):
        """Moves file to a new target.
        Target string is substituted according to ``pathmap`` rules.
        """
        newp = self.pathmap(pattern)
        shutil.move(self, newp, copy_function=copy_function)
        return newp

    def open(self, *args, **kwargs):
        """Wrapper around ``open``."""
        return open(self, *args, **kwargs)

    def chdir(self):
        """Wrapper around ``os.chdir``."""
        # TODO: context processor
        os.chdir(self)

    def chmod(self, mode, **kwargs):
        """Wrapper around ``os.chmod``."""
        os.chmod(self, mode, **kwargs)

    def chown(self, owner=None, group=None):
        """Change path owner."""
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
