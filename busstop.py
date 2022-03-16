#!/usr/bin/env python3

import datetime
from requests import get
import time
import json

starttime = time.time()

while True:
    data = get(
        'https://api.tfl.gov.uk/StopPoint/910GRCTRYRD/ArrivalDepartures?lineIds=london-overground&bus')
    # hkrules = r.text
    # filtered = list(
    #     filter(lambda i: i['destinationNaptanId'] == "910GENFLDTN"))
    # json.dumps(data.text).sort(
    #     key=lambda x: x.estimatedTimeOfDeparture, reverse=False)

    data_dict = json.loads(data.text)

    # print(data.text.sort(
    #     key=lambda x: x.estimatedTimeOfDeparture)
    # )

    for x in data_dict:
        print(x['destinationName'], ':'),
        print('| * ~ * |', datetime.datetime.strptime(
            x['estimatedTimeOfDeparture'], '%Y-%m-%dT%H:%M:%SZ').time(), '| * ~ * |')

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
