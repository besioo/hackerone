#!/usr/bin/env python
import requests
import os
import csv
from termcolor import *


# change the path to your current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main(x=1,y=1500000,report="reports.csv"):
    """
    This function will get the reports from the API and write them to a file.
    x and y are the starting and ending numbers of the reports to be retrieved.
    report is the name of the file to write the reports to.
    """
    output_file = open(report, "a")
    csv_writer = csv.writer(output_file)
    for _id in range(x,y):

      response = requests.get(f"https://api.hackerone.com/v1/hackers/reports/{_id}",
          auth=('ahmed_basiony', ''),
          headers = {"Accept": "application/json"},
          timeout=10)

      # convert the response to a json object
      report = response.json()
      # check if the response is valid
      if report.get("data",""):
              # get the report data
            report_data = {}
            report_data['id'] = report['data']['id']
            report_data['title'] = report['data']['attributes']['title']
            report_data['status'] = report['data']['attributes']['state']
            report_data['link'] = f"https://hackerone.com/reports/{report['data']['id']}"
            # write the report data to the file
            csv_writer.writerow(report_data.values())
            cprint(f"[+] {str(_id)} Success!", 'green')
      else:
            cprint(f"[-] {str(_id)} Failed!", 'red')
            continue

