import requests
import json
from monitoring.test_data import *


# New draft only
def draft_monitoring():

    monitoring_id = requests.post('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings', data=json.dumps(payload), headers=headers)
    monitoring_id_long = monitoring_id.json()['data']['id']
    monitoring_id_short = monitoring_id.json()['data']['monitoring_id']
    return monitoring_id_long, monitoring_id_short
#print(draft_monitoring())


# New monitoring + activation
def active_monitoring():

    monitoring_id = draft_monitoring()
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings' + '/' + monitoring_id, data=json.dumps(payload2), headers=headers)
    resp = requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings' + '/' + monitoring_id, data=json.dumps(activate), headers=headers)
    return resp.json()['data']['id']
#print(active_monitoring())


# New monitoring + 5 posts
def post_monitoring():
    monitoring_id = active_monitoring()
    for i in range(5):
        requests.post('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id + '/' + 'posts', data=json.dumps(msg), headers=headers)
    return monitoring_id


# New monitoring ---> activate ----> addressed
def make_conclusion_and_adress():

    monitoring_id = post_monitoring()
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id, data=json.dumps(conclusion), headers=headers)
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id, data=json.dumps(adressed), headers=headers)
    return monitoring_id

# New monitoring: draft ---> activate ----> declined
def make_conclusion_for_declined():
    monitoring_id = post_monitoring()
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id, data=json.dumps(conclusion_for_declined), headers=headers)
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id, data=json.dumps(decline), headers=headers)
    return monitoring_id
#print(make_conclusion_for_declined())


# New monitoring ---> activate ----> addressed ---> stopped
def stop_monitoring():
    monitoring_id = make_conclusion_and_adress()
    resp = requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings' + '/' + monitoring_id, data=json.dumps(stopped), headers=headers)
    return monitoring_id


# New monitoring ---> activate ----> addressed ---> complete
def complete_monitoring():
    monitoring_id = make_conclusion_and_adress()
    resp = requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings' + '/' + monitoring_id,
                          data=json.dumps(complete), headers=headers)
    return resp.json()


# New monitoring ---> activate ----> declined ---> closed
def close_monitoring():
    monitoring_id = active_monitoring()
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id,
                   data=json.dumps(conclusion), headers=headers)
    requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings/' + monitoring_id,
                   data=json.dumps(eliminationResolution), headers=headers)
    resp = requests.patch('https://audit-api-sandbox.prozorro.gov.ua/api/2.4/monitorings' + '/' + monitoring_id,
                          data=json.dumps(decline), headers=headers)

    return resp.json()

print(draft_monitoring())