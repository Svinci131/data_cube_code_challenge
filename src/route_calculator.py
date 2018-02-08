"""
  This file contatins a function used to calculate the distance
  and time for most efficient path between a series of locations.

"""

from datetime import datetime, timedelta
from src.flight_data_calculator import get_flight_distance_in_meters, \
    get_flight_duration_in_secs
from src.google_utils import get_distance_matrix


def get_most_efficient_route(locations):
    """
    :type routes: list
    :rtype: dict
      { distance: int,
        time: int }
    """
    distance_matrix = get_distance_matrix('|'.join(locations))
    rows = distance_matrix.get('rows', None)

    paths = []

    for i, location in enumerate(locations):
      if (i != 0):
        row = rows[0]
        elements = row.get('elements', [])
        try:
          dist = _get_distance(elements[i], locations[0], location)
          time = _get_time(elements[i], dist)
          newPaths = _find_paths(i, locations, [0], rows)

          for newPath in newPaths:
            paths.append({
              'distance': dist + newPath.get('distance'),
              'time': time + newPath.get('time')
            })

        except BaseException as e:
          print('ERROR', str(e))
          raise Exception(error)

    fastest_path_data = _get_fastest_path(paths)

    return {
        'distance': _format_distance(fastest_path_data.get('distance')),
        'time': _format_time(fastest_path_data.get('time'))
    }

def _find_paths(nodeIndx, locations, visited, matrix):
  visited = visited + [nodeIndx]
  location = locations[nodeIndx]
  row = matrix[nodeIndx]
  elements = row.get('elements', [])
  paths = []

  for i, subnode in enumerate(elements):
    if i not in visited:
      nextLocation = locations[i]
      dist = _get_distance(elements[i], location, nextLocation)
      time = _get_time(elements[nodeIndx], dist)
      newPaths = _find_paths(i, locations, visited, matrix)

      for newPath in newPaths:
        paths.append({
          'distance': dist + newPath.get('distance'),
          'time': time + newPath.get('time')
        })
      
  if (len(paths) == 0) :
    # Add distance back to origin at end
    dist = _get_distance(elements[nodeIndx], locations[0], location)
    time = _get_time(elements[nodeIndx], dist)
    return [{ 'distance': dist, 'time': time }]

  return paths

def _get_distance(element, origin, nextDest):
  """
  Get the distance in meters of the path between two points.
  Either using the element object from the google distance matrix
  or calculating the shortest flight route.

  :type element: dict
  :rtype: int
  """
  status = element.get('status', None)
  if (status == 'OK'):
      """
      If a drivable route is found use
      the distance of the roads between those locations.
      """
      dist = element.get('distance', {}).get('value', None)
  elif (status == 'ZERO_RESULTS'):
      """
        Google maps needs travelmode and
        "flight" is not an option so if driving isn't possible
        calculate with the Haversine Formula.
      """
      print('No Driving Route, Calculating Flight...')
      dist = get_flight_distance_in_meters(origin, nextDest)  # meters
  else:
      raise Exception('Something went wrong')

  return dist

def _get_time(element, distance):
  """
  Get the time in seconds it will take to go between two points.
  Either using the element object from the google distance matrix
  or calculating the flight time if no drivable route is found.

  :type element: dict
  :rtype: int
  """
  status = element.get('status', None)
  if (status == 'OK'): # if a drivable route is found
      time = element.get('duration', {}).get('value', None)
  elif (status == 'ZERO_RESULTS'):
      time = get_flight_duration_in_secs(distance)  # secs
  else:
      raise Exception('Something went wrong')

  return time

def _get_fastest_path(paths):
  """
  Takes a list of dictionaries with path data
  ex. { 'distance': 10236813, 'time': 168808 }
  and the path with the shortest distance.

  :type paths: list[dict] 
  :rtype: dict
  """
  fastest_path = None

  for path in paths:
    if fastest_path is None:
      fastest_path = path
    elif fastest_path.get('distance') > path.get('distance'):
      fastest_path = path

  return fastest_path

def _format_distance(meters):
    """
    Takes the number of meters,
    converts it to kilometers if there
    is more than one meters and returns a 
    returns a formatted string with the unit type.

    :type meters: int
    :rtype: str
    """
    if (meters > 1000):
        return '{} km'.format(meters / 1000)
    else:
        return '{} meters'.format(meters)


def _format_time(seconds):
    """
    Convert time from number of seconds 
    to a formatted string with days,
    hours, minutes, and seconds.

    :type seconds: int
    :rtype: str
    """
    sec = timedelta(seconds=int(seconds))
    d = datetime(1, 1, 1) + sec
    return '{} days {} hours {} minutes {} seconds'.format(
        d.day - 1, d.hour, d.minute, d.second)

