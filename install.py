import launch

if not launch.is_installed("pycloudflared"):
    launch.run_pip("install pycloudflared", "pycloudflared")
