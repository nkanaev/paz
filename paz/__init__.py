import os
import re


__version__ = '0.0.1'


class p(str):
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
