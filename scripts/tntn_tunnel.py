# Note: tntn is also my package. https://github.com/Bing-su/tntn
from tntn import bore, jprq

from discord_webhook import send_to_discord
from modules.shared import cmd_opts

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
    bore_urls = bore(port)

    if cmd_opts.tunnel_webhook:
        send_to_discord(bore_urls.tunnel, cmd_opts.tunnel_webhook)
