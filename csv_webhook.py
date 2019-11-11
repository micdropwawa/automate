import csv
import time
import requests

# Reading csv file with 2 columns: 1st column "Name", 2nd column "Phone"
csv_file = ('/PATH_TO_CSV_FILE')

with open(csv_file) as f:
    reader = csv.reader(f, delimiter=',')
    # Disregard top row
    next(f)
    for row in reader:
        url = ("https://flows.messagebird.com/flows/FLOW-ID/invoke?name=" + row[0] + "&phone=" + row[1] + "&url=" + row[2])
        print(url)
        with requests.get(url) as response:
            if response.status_code == 204:
                print('204 ' + 'Success!')
            elif response.status_code == 200:
                print('200 ' + 'Success!')
            elif response.status_code == 404:
                print('404 ' + 'Not Found.')
        # Pausing for 0.2 seconds between each loop/call
        time.sleep(0.2)