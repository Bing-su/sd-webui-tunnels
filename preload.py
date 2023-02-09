import argparse


def preload(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--cloudflared",
        action="store_true",
        help="use trycloudflare, alternative to gradio --share",
    )
