from __future__ import annotations

import atexit
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from discord_webhook import send_to_discord
from modules.shared import cmd_opts

LOCALHOST_RUN = "localhost.run"
REMOTE_MOE = "remote.moe"
localhostrun_pattern = re.compile(r"(?P<url>https?://\S+\.lhr\.life)")
remotemoe_pattern = re.compile(r"(?P<url>https?://\S+\.remote\.moe)")


def gen_key(path: str | Path) -> None:
    path = Path(path)
    args = [
        "ssh-keygen",
        "-t",
        "rsa",
        "-b",
        "4096",
        "-q",
        "-f",
        path.as_posix(),
        "-N",
        "",
    ]
    subprocess.run(args, check=True)
    path.chmod(0o600)


def ssh_tunnel(host: str = LOCALHOST_RUN) -> str:
    ssh_name = "id_rsa"
    ssh_path = Path(__file__).parent.parent / ssh_name

    tmp = None
    if not ssh_path.exists():
        try:
            gen_key(ssh_path)
        # write permission error or etc
        except subprocess.CalledProcessError:
            tmp = TemporaryDirectory()
            ssh_path = Path(tmp.name) / ssh_name
            gen_key(ssh_path)

    port = cmd_opts.port if cmd_opts.port else 7860

    args = [
        "ssh",
        "-R",
        f"80:127.0.0.1:{port}",
        "-o",
        "StrictHostKeyChecking=no",
        "-i",
        ssh_path.as_posix(),
        host,
    ]

    tunnel = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8"
    )

    atexit.register(tunnel.terminate)
    if tmp is not None:
        atexit.register(tmp.cleanup)

    tunnel_url = ""
    lines = 27 if host == LOCALHOST_RUN else 5
    pattern = localhostrun_pattern if host == LOCALHOST_RUN else remotemoe_pattern

    for _ in range(lines):
        line = tunnel.stdout.readline()
        if line.startswith("Warning"):
            print(line, end="")

        url_match = pattern.search(line)
        if url_match:
            tunnel_url = url_match.group("url")
            break
    else:
        raise RuntimeError(f"Failed to run {host}")

    print(f" * Running on {tunnel_url}")
    return tunnel_url


if cmd_opts.localhostrun:
    print("localhost.run detected, trying to connect...")
    lhr_url = ssh_tunnel(LOCALHOST_RUN)

    if cmd_opts.tunnel_webhook:
        send_to_discord(lhr_url, cmd_opts.tunnel_webhook)

if cmd_opts.remotemoe:
    print("remote.moe detected, trying to connect...")
    moe_url = ssh_tunnel(REMOTE_MOE)

    if cmd_opts.tunnel_webhook:
        send_to_discord(moe_url, cmd_opts.tunnel_webhook)
