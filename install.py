import launch

if not launch.is_installed("pycloudflared"):
    launch.run_pip("install pycloudflared", "pycloudflared")

if not launch.is_installed("tntn"):
    launch.run_pip("install tntn", "tntn")
