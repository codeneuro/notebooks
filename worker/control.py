import sys
import yaml 
import requests

PUBLIC_IP_URL = "http://169.254.169.254/latest/meta-data/public-ipv4"
CONF_FILE = "conf.yml"

def get_public_ip(settings): 
    return requests.get(PUBLIC_IP_URL).text + ':' + settings['worker']['port']

def get_master_url(settings): 
    return settings['master']['host'] + ':' + settings['master']['port'] + '/hosts'

def start(settings): 
    public_ip = get_public_ip(settings)
    url = get_master_url(settings)
    payload = {"host": public_ip}
    requests.post(url, data=payload)

def stop(settings): 
    public_ip = get_public_ip(settings)
    url = get_master_url(settings)
    payload = {"host": public_ip}
    requests.delete(url, data=payload)

if __name__ == "__main__": 
    cmd = sys.argv[1]
    settings = yaml.load(open(CONF_FILE, 'r'))
    if cmd == 'start': 
        start(settings)
    elif cmd == 'stop': 
        stop(settings)
