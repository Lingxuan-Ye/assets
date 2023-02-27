#!/usr/bin/env python

import subprocess
import sys
from pathlib import Path

import pyperclip
from hash_rename import rename

DIRS = [
    Path('./images/general/'),
    Path('./images/chat_log/')
]

def main() -> None:

    force_all = True if sys.argv[0].lower() == '--force-all' else False

    files: list[Path] = []

    for dir in DIRS:
        for i in dir.rglob('*'):
            if not i.is_file():
                continue
            if force_all:
                files.append(i)
                continue
            if i.stem.isalnum() and len(i.stem) == 64 and i.name.islower():
                continue
            files.append(i)

    clipboard: list[str] = []

    for i in Path(__file__).resolve().parents:
        if i.name == 'scripts':
            root = i.parent
            break

    for file in files:
        clipboard.append(
            '![](https://raw.githubusercontent.com/Lingxuan-Ye'
            f'/assets/main/{rename(file)[0].relative_to(root).as_posix()})'
        )

    pyperclip.copy('\n\n'.join(clipboard))

    subprocess.run('git add -A')
    subprocess.run('git commit -q -m "Upload"')
    subprocess.run('git push -f')


if __name__ == '__main__':
    main()
