import json
import os

def airports_tojson(file_name):
    airports = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            start, end = None, -1
            while True:
                start = line.find(r'"', end + 1)
                if start == -1:
                    break
                end = line.find(r'"', start + 1)
                line = line[:start] + line[start:end].replace(',', '\x00') + line[end:]
            line = line.split(',')
            line = map(lambda x: x.replace('\x00', ','), line)
            line = map(lambda x: x.strip(r'"'), line)
            line = map(lambda x: x if x != r'\N' else None, line)
            # print line
            airports.append({
                'pk': int(line[0]),
                'model': 'flights_app.Airport',
                'fields':{
                    'name': line[1],
                    'city': line[2],
                    'country': line[3],
                    'IATA_code': line[4],
                    'ICAO_code': line[5],
                    'lat': float(line[6]),
                    'lon': float(line[7]),
                    'alt': int(line[8]),
                    'timezone': float(line[9]),
                    'DST': line[10]
                }
            })
    with open(os.path.dirname(file_name) + os.path.sep + 'airports.json', 'w') as file:
        json.dump(airports, file, indent=4)

def routes_tojson(file_name):
    def handle_null(s):
        try:
            return int(s)
        except TypeError as e:
            print e
            return None

    airports = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            start, end = None, -1
            while True:
                start = line.find(r'"', end + 1)
                if start == -1:
                    break
                end = line.find(r'"', start + 1)
                line = line[:start] + line[start:end].replace(',', '\x00') + line[end:]
            line = line.split(',')
            line = map(lambda x: x.replace('\x00', ','), line)
            line = map(lambda x: x.strip(r'"'), line)
            line = map(lambda x: x if x != r'\N' else None, line)
            # print line
            airports.append({
                'model': 'flights_app.Route',
                'fields':{
                    'airline_code': line[0],
                    'airline_id': handle_null(line[1]),
                    'source_code': line[2],
                    'source_id': handle_null(line[3]),
                    'dest_code': line[4],
                    'dest_id': handle_null(line[5]),
                    'codeshare': line[6],
                    'stops': int(line[7]),
                    'equipment': line[8],
                    }
            })
    with open(os.path.dirname(file_name) + os.path.sep + 'routes.json', 'w') as file:
        json.dump(airports, file, indent=4)


if __name__ == '__main__':
    airports_tojson('./airports.dat')
    routes_tojson('./routes.dat')