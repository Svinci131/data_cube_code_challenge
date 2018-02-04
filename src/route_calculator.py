"""
  This file contatins a function used to calculate the distance
  and time for most efficient path between a series of locations.

"""

from src.flight_data_calculator import get_flight_distance_in_meters, get_flight_duration_in_secs
from src.google_utils import get_distance_matrix
from datetime import datetime, timedelta

def _format_distance(meters):
  if (meters > 1000):
    return '{} km'.format(meters/1000)
  else:
    return '{} meters'.format(meters)

def _format_time(seconds):
  sec = timedelta(seconds=int(seconds))
  d = datetime(1,1,1) + sec
  return '{} days {} hours {} minutes {} seconds'.format(d.day-1, d.hour, d.minute, d.second)

def get_most_efficient_route(locations):
    """
    :type routes: list
    :rtype: dict
      { distance: int,
        time: int }
    """
    distance_matrix = get_distance_matrix('|'.join(locations))
    rows = distance_matrix.get('rows', None)

    total_distance_in_meters = 0
    total_time_in_seconds = 0

    for i, row in enumerate(rows):
      elements = row.get('elements')
      origin = locations[i]
      j = i + 1
      if (j != len(locations)): # Not the final destination
        element = elements[j]
        dest = locations[j]
        status = element.get('status', None)

        if (status == 'OK'):
          # if a drivable route is found between those locations
          dist = element.get('distance', {}).get('value', None)
          time = element.get('duration', {}).get('value', None)
        elif (status == 'ZERO_RESULTS'):
          """
            Google maps needs travelmode and
            "flight" is not an option so if driving isn't possible
            calculate with the Haversine Formula.
          """
          print('No Driving Route, Calculating Flight...')
          dist = get_flight_distance_in_meters(origin, dest) #meters
          time = get_flight_duration_in_secs(dist) #secs
        else:
          raise Exception('Something went wrong')


        print(origin, '->', dest, 'dist', dist, 'time', time)
        total_distance_in_meters += dist
        total_time_in_seconds += time

    return {
      'distance': _format_distance(total_distance_in_meters),
      'time': _format_time(total_time_in_seconds)
    }

