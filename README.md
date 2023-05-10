# sd-webui-tunnels

Tunneling extension for [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

## Usage

### [cloudflared](https://try.cloudflare.com/)

add `--cloudflared` to commandline options.

### [localhost.run](https://localhost.run/)

add `--localhostrun` to commandline options.

### [remote.moe](https://github.com/fasmide/remotemoe)

add `--remotemoe` to commandline options.

The feature of `remote.moe` is that as long as the same ssh key is used, the same url is generated.

The ssh keys for `localhost.run` and `remote.moe` are created with the name `id_rsa` in the script's root folder. However, if there is a problem with the write permission, it is created in a temporary folder instead, so a different url is created each time.

### [jprq](https://github.com/azimjohn/jprq)

add `--jprq "YOUR_JPRQ_TOKEN"` to commandline options.

You can get a token [here](https://jprq.io/auth).

### [bore](https://github.com/ekzhang/bore)

add `--bore` to commandline options.

add `--bore_url "URL"` for custom bore url. url without 'http://' and (optional) port. example: myboreserver.com or myboreserver.com:12345

### googleusercontent

add `--googleusercontent` to commandline options. It must be used with `--no-gradio-queue`, otherwise it will not work.

If not in google colab, it will be ignored.

-----
### Discord webhook

add `--tunnel-webhook <webhookurl>` to commandline options.

This feature was taken from [nur-zaman/sd-webui-tunnels](https://github.com/nur-zaman/sd-webui-tunnels) fork. thanks.
