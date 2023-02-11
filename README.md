# Dropper. A kittypaws plugin

A plugin to drop connection of a certain container to a certain IP address with the use of [kittypaws](https://github.com/subatiq/kittypaws).

## Installation

Put the `run.sh` into `~/.kittypaws/plugins/dropper` folder.

## Example config

```yaml
plugins:
- dropper:
    target: mmcv_traffic-npd_1
    ip: 192.168.10.10
    unavailable_seconds: 1800
    frequency: random
    min_interval: PT1H
    max_interval: PT90M
```

`target` - container in which disconnection should be simulated\
`ip` - which address to disconnect\
`unavailable_seconds` - amount of time the `ip` will be unavailable for the `target`
