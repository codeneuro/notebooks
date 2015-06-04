import sys
import yaml 
import json
import requests

CONF_FILE = "conf.yml"

def get_host_and_port(settings): 
    return settings['worker']['host'] + ':' + str(settings['worker']['port'])

def get_master_url(settings): 
    return settings['master']['host'] + ':' + str(settings['master']['port']) + '/hosts'

def start(settings): 
    public_ip = get_host_and_port(settings)
    url = get_master_url(settings)
    payload = {"host": public_ip}
    requests.post(url, data=json.dumps(payload))

def stop(settings): 
    public_ip = get_host_and_port(settings)
    url = get_master_url(settings)
    payload = {"host": public_ip}
    requests.delete(url, data=json.dumps(payload))

if __name__ == "__main__": 
    cmd = sys.argv[1]
    settings = yaml.load(open(CONF_FILE, 'r'))
    if cmd == 'start': 
        start(settings)
    elif cmd == 'stop': 
        stop(settings)
