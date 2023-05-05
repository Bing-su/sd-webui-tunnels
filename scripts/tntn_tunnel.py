# Note: tntn is also my package. https://github.com/Bing-su/tntn
from tntn import bore, jprq

from discord_webhook import send_to_discord
from modules.shared import cmd_opts


def bore_url(s: str):
    if ":" in s:
        host, port = s.split(":")
        port = int(port)
    else:
        host = s
        port = None
    return host, port


port = cmd_opts.port if cmd_opts.port else 7860

if cmd_opts.jprq:
    # jprq will raise an error unless that port is actually running.
    import modules.script_callbacks as script_callbacks

    def jprq_callback(*args, **kwargs):
        jprq_urls = jprq(port, cmd_opts.jprq)

        if cmd_opts.tunnel_webhook:
            send_to_discord(jprq_urls.tunnel, cmd_opts.tunnel_webhook)

    script_callbacks.on_app_started(jprq_callback)

if cmd_opts.bore:
    host, bore_port = bore_url(cmd_opts.bore_url) if cmd_opts.bore_url else (None, None)
    kwargs = {}
    if host is not None:
        kwargs["bore_url"] = host
    if bore_port is not None:
        kwargs["bore_port"] = bore_port
    bore_urls = bore(port, **kwargs)

    if cmd_opts.tunnel_webhook:
        send_to_discord(bore_urls.tunnel, cmd_opts.tunnel_webhook)
