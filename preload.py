import argparse


def preload(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--cloudflared",
        action="store_true",
        help="use trycloudflare, alternative to gradio --share",
    )

    parser.add_argument(
        "--localhostrun",
        action="store_true",
        help="use localhost.run, alternative to gradio --share",
    )

    parser.add_argument(
        "--remotemoe",
        action="store_true",
        help="use remote.moe, alternative to gradio --share",
    )

    parser.add_argument(
        "--jprq",
        type=str,
        help="use jprq, alternative to gradio --share, requires a token. https://jprq.io/auth",
    )

    parser.add_argument(
        "--bore",
        action="store_true",
        help="use bore, alternative to gradio --share",
    )

    parser.add_argument(
        "--bore_url",
        type=str,
        help="custom bore url. url without 'http://' and (optional) port. example: myboreserver.com or myboreserver.com:12345",
    )

    parser.add_argument(
        "--googleusercontent",
        action="store_true",
        help="use googleusercontent, only available in the google colab. must be used with --no-gradio-queue",
    )

    parser.add_argument(
        "--tunnel-webhook", type=str, help="discord webhook to send tunnel url to"
    )
