#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jaraco.windows==3.4','console_scripts','gclip'
__requires__ = 'jaraco.windows==3.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('jaraco.windows==3.4', 'console_scripts', 'gclip')()
    )
