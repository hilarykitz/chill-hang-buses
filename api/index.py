from http.server import BaseHTTPRequestHandler
from requests import get
import datetime
import time
import json

starttime = time.time()


def sortTime(k):
    if k:
        return k['estimatedTimeOfArrival']
    return k


def stripDateTime(d): return datetime.datetime.strptime(
    d, '%Y-%m-%dT%H:%M:%SZ').time()


def printBuses(stop):
    bus_lines = ['253', '106', '254', '393', 'N253']
    print('Stop', stop)
    our_stops = []
    for line in bus_lines:
        path = 'https://api.tfl.gov.uk/Line/' + line + '/Arrivals'
        busData = get(path)

        bus_dict = json.loads(busData.text)
        our_stops += list(filter(lambda x: x['platformName']
                          == stop, bus_dict))
    print(our_stops)
    return our_stops

    # for index, b in enumerate(our_stop):
    #     if index < 2:
    #         print(b['lineName'], 'to', b['towards'],
    #               stripDateTime(b['expectedArrival']))
    #     else:
    #         return


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # while True:
        data = get(
            'https://api.tfl.gov.uk/StopPoint/910GRCTRYRD/ArrivalDepartures?lineIds=london-overground&bus')

        data_dict = json.loads(data.text)

        # data_dict.sort(key=sortTime)
        # print('<==Overground==>')
        # for x in data_dict:
        #     print(x['destinationName'], ':'),
        #     print('| * ~ * |',
        #           stripDateTime(x['estimatedTimeOfArrival']), '| * ~ * |')

        # print('<==Buses==>')
        # printBuses('O')
        # printBuses('B')

        return [data_dict, printBuses('0'), printBuses('B')]

        # time.sleep(60.0 - ((time.time() - starttime) % 60.0))


# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(str('Hello World!!').encode())
#         return
