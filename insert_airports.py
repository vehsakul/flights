#!/usr/bin/python
import psycopg2 as db
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--host', default='localhost', dest='host')
parser.add_argument('-u', '--user', required=True, dest='user')
parser.add_argument('--db', required=True, dest='db')
args = parser.parse_args()
password = raw_input('Enter password:')

conn = db.connect(database=args.db, user=args.user, password=password, host=args.host)

# ROUTES TABLE:
# Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
# Airline ID	Unique OpenFlights identifier for airline (see Airline).
# Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
# Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
# Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
# Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
# Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
# Stops	Number of stops on this flight ("0" for direct)
# Equipment	3-letter codes for plane type(s) generally used on this flight, separated by spaces

# AIRPORTS TABLE:
# Airport ID	Unique OpenFlights identifier for this airport.
# Name	Name of airport. May or may not contain the City name.
# City	Main city served by airport. May be spelled differently from Name.
# Country	Country or territory where airport is located.
# IATA/FAA	3-letter FAA code, for airports located in Country "United States of America".
# 3-letter IATA code, for all other airports.
# Blank if not assigned.
# ICAO	4-letter ICAO code.
# Blank if not assigned.
# Latitude	Decimal degrees, usually to six significant digits. Negative is South, positive is North.
# Longitude	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
# Altitude	In feet.
# Timezone	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
# DST	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
