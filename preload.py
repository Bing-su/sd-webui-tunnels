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
        "--tunnel-webhook", type=str, help="discord webhook to send tunnel url to"
    )
