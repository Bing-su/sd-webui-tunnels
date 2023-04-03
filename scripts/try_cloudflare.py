# Note: pycloudflared is also my package. https://github.com/Bing-su/pycloudflared
from pycloudflared import try_cloudflare

from discord_webhook import send_to_discord
from modules.shared import cmd_opts

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860

    urls = try_cloudflare(port)
    if cmd_opts.tunnel_webhook:
        send_to_discord(urls.tunnel, cmd_opts.tunnel_webhook)
