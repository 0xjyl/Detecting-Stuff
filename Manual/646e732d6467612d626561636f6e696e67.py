# Custom script to create fake web requests to suspected domain generated algorithm domains 

import random
import string
import subprocess
import time 

def gen_fake_dga():
    len = random.randint(8, 64)
    
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k = len))

    tld = random.choice(['.com', '.net', '.org', '.co','.info', '.online', '.xyz', '.io'])

    return domain + tld

def request_fake_dga(domain):
    try:
        result = subprocess.run(['nslookup', domain], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        print(result.stdout)
    except Exception as e : 
            print(f"Error Occurred: {e}")

def req_int(requests=4, interval=300):
        for _ in range(requests):
              fake_dga = gen_fake_dga()
              print(f"Sending DNS requests: {fake_dga}")
              request_fake_dga(fake_dga)
              if _ < requests -1: 
                    time.sleep(interval / requests)
req_int()


