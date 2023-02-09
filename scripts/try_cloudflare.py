from pycloudflared import try_cloudflare

from modules.shared import cmd_opts

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    try_cloudflare(cmd_opts.port)
