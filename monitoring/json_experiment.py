import requests
import json
import pprint
from monitoring.test_data import *

def draft_and_active_monitoring():
    print("Create monitoring...")
    monitor_id_long = requests.post('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings', data=json.dumps(payload), headers=headers)

    return monitor_id_long.json()['data']['id']

#print("Monitoring ID: {}".format(draft_and_active_monitoring()))
print("{} {} {}".format("skdjsfkj", 514155, 1515))
#print("skdjsfkj" + 514155)