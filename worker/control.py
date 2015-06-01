import sys
import yaml 
import requests

PUBLIC_IP_URL = "http://169.254.169.254/latest/meta-data/public-ipv4"
CONF_FILE = "conf.yml"

def get_public_ip(): 
    return requests.get(PUBLIC_IP_URL)

def get_master_url(settings): 
    return settings['master']['host'] + ':' + settings['master']['port']

def start(settings): 
    public_ip = get_public_ip()
    url = get_master_url(settings)
    payload = {"host": public_ip}
    requests.post(url, data=payload)

def stop(settings): 
    public_ip = get_public_ip()
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
