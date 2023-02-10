from __future__ import annotations

import shlex
import subprocess
from pathlib import Path


def gen_key(path: str | Path) -> None:
    arg_string = f'ssh-keygen -t rsa -b 4096 -N "" -f {path}'
    args = shlex.split(arg_string)
    subprocess.run(args, check=True)
