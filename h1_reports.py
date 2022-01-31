import requests
import json
from termcolor import *

output_file = open("reports.csv", "a")

headers = {
  'Accept': 'application/json'
}

for id in range(1,1500000):
  r = requests.get(
      f"https://api.hackerone.com/v1/hackers/reports/{id}",
      auth=('ahmed_basiony', ''),
      headers = headers,
      timeout=10
  )

  report = json.loads(r.text)
  try:
     report['data']
  except:
     cprint(f"[-] {str(id)} Failed!", 'red')
     continue
  else:
     report_id = report['data']['id']
     report_title = report['data']['attributes']['title']
     report_state = report['data']['attributes']['state']
     link = f"https://hackerone.com/reports/{report_id}"
     output_file.write(f"{id}, {link}, {report_title}, {report_state}\n")
     cprint(f"[+] {str(id)} Success!", 'green')

output_file.close()

