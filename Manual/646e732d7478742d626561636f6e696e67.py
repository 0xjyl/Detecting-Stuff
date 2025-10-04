#DNS TXT RECORD BEACONING TEST 


import subprocess
import time

domain = "3xzu2h.0.232.hbqetbnzefagnoegnkktambqgaydanjtmezdcyocwo4owrslsc6rlsap6iea4oy.umxub3z7lcqy55gpjsevxhtgmgfrepri7ofb7jikfr4t7kecl5cunsb5vckxsu5.i73h7n5ynja476j2ifpiglyu7pw6zwtfq4f3zk3bozbhws3ay2bzuvqpfbpixvv.4pjfteeouz7weamzm3r5v3w4ohy4y.0ecad238.cnr.io"
rec_type = "TXT "
count = 15
interval = 20

def dns_req(domain, rec_type):
     try: 
          subprocess.run(['nslookup', '-type=TXT', domain], check=True)
          print(f"DNS TXT Record query sent for {domain}")
     except subprocess.CalledProcessError as e:
        print(f"An error has occurred for the request: {e}.")

for _ in range(count):
      dns_req(domain, rec_type)
      time.sleep(interval)

print("Finished generating DNS TXT queries")