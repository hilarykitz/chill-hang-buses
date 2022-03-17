import json
import time
import datetime
from requests import get
from flask import Flask, render_template
app = Flask(__name__)

# starttime = time.time()


def sortTime(k):
    if k:
        return k['estimatedTimeOfArrival']
    return k


# def stripDateTime(d): return datetime.datetime.strptime(
#     d, '%Y-%m-%dT%H:%M:%SZ').time()


def getBuses(stop):
    bus_lines = ['253', '106', '254', '393', 'N253']

    our_stops = []
    for line in bus_lines:
        path = 'https://api.tfl.gov.uk/Line/' + line + '/Arrivals'
        busData = get(path)

        bus_dict = json.loads(busData.text)
        our_stops += list(filter(lambda x: x['platformName']
                          == stop, bus_dict))

    # for index, b in enumerate(our_stops):
    #     if index < 2:
    #         busOutput += b['lineName'], 'to', b['towards'],
    #         stripDateTime(b['expectedArrival'])
    #     else:
    #         return

    return our_stops


def getAllBuses():
    allbuses = getBuses('0'), getBuses('B')
    return allbuses


def getTrains():
    output = ''
    # while True:
    data = get(
        'https://api.tfl.gov.uk/StopPoint/910GRCTRYRD/ArrivalDepartures?lineIds=london-overground&bus')

    data_dict = json.loads(data.text)
    data_dict.sort(key=sortTime)

    return data_dict

    # output += '<==Overground==>'
    # for x in data_dict:
    #     output += x['destinationName'], ':', '| * ~ * |',
    #     stripDateTime(x['estimatedTimeOfArrival']), '| * ~ * |'

    # output += '<==Buses==>'
    # output += printBuses('O')
    # output += printBuses('B')

    # return output

    # time.sleep(60.0 - ((time.time() - starttime) % 60.0))


@app.route("/")
def hello_world():
    trainData = getTrains()
    busData = getAllBuses()

    print(trainData)
    return render_template('template.html', trainData=trainData, busData=busData)
