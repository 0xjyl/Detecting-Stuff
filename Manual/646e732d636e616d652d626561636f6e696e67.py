#DNS CNAME BEACONING TEST

import subprocess
import time

cname = "releasescloudproxy.cloud.com"
count = 15
interval = 20 / count

def dns_req(domain):
    try:

        result = subprocess.run(['nslookup', '-type=CNAME', domain], capture_output=True, text=True)
        print(result.stdout)

    except Exception as e:
        print(f"An Error has occurred: {e}")

for _ in range(count):
    dns_req(cname)
    if _ < count - 1: 
        time.sleep(interval)
    
print("Finished generating DNS CNAME queries")

