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
