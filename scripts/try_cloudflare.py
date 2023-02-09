from pycloudflared import try_cloudflare

from modules.shared import cmd_opts

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    try_cloudflare(port)
