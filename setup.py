import sys
from cx_Freeze import setup, Executable

includefiles = []
includes = []
excludes = []
packages = []

setup(
    name = 'myapp',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'lenin',
    author_email = 'le...@null.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('PySv.py')]
)
