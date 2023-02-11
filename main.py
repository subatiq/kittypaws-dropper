import time
from typing import Dict
from subprocess import check_output, CalledProcessError

def run(config: Dict[str, str]) -> None:
    target = config.get('target')
    ip = config.get('ip')
    unavailable_seconds = int(config.get('unavailable_seconds', 10))

    print('Checking if iptables are available...')
    try:
        check_output(f'docker exec {target} apt-get install iptables -y', shell=True)
    except CalledProcessError as e:
        print("Problem while trying to install iptables:", e)
        return

    try:
        check_output(f"docker exec {target} bash -c 'iptables -C OUTPUT -d {ip} -j DROP || iptables -I OUTPUT -d {ip} -j DROP'", shell=True)
        print(f'--- {ip} is unavailable now for {target}. Switching in {unavailable_seconds} sec')
    except Exception as e:
        print("Can't turn off connection, probably container is dead", e)

    time.sleep(unavailable_seconds)

    try:
        check_output(f"docker exec {target} bash -c 'iptables -D OUTPUT -d {ip} -j DROP'", shell=True)
        print(f'+++ {ip} is available now for {target}. Switching off in the next run')
    except Exception as e:
        print("Can't turn on connection, probably container is dead", e)
