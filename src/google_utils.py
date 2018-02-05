"""
  This file contains helper functions for calling the
  Google maps API and formatting the responses.

"""

import json
from urllib.request import urlopen
from src.config import API_KEY

ROOT_URL = "https://maps.googleapis.com/maps/api/"


def get_distance_matrix(locations):
    """
      Call the google maps API to rerieve the distance
      and time of trip between each city.

      :type locations: str
      :rtype: dict
    """

    opts = {
        'key': API_KEY,
        'origins': locations,
        'destinations': locations
    }

    params = '&'.join(['{}={}'.format(key, opts[key]) for key in opts.keys()])
    url = ROOT_URL + 'distancematrix/json?' + params
    res = urlopen(url)
    data = json.load(res)

    if (data.get('status', None) != 'OK'):
        error = data.get('error_message', 'Something went wrong')
        print('ERROR FETCHING DISTANCE MATRIX', error)
        raise Exception(error)

    return data


def get_geocode(address):
    """
      Call the google maps API to rerieve
      the lng/lat of a given address or location.

      :type locations: str
      :rtype: dict
    """
    url = ROOT_URL + 'geocode/json?address=' + address
    res = urlopen(url)
    data = json.load(res)

    if (data.get('status', None) == 'OK'):
        geoLocation = data.get('results', [])[0].get('geometry', {})
        location = geoLocation.get('location', {})

        if (_missing_lat_lon(location)):
            raise Exception('Could not get geolocation for {}'.format(address))
        return location
    else:
        error = data.get('error_message', 'Something went wrong')
        print('ERROR FETCHING GEOCODE', error)
        raise Exception(error)


def _missing_lat_lon(location):
    if ('lat' not in location or 'lng' not in location):
        return True
    else:
        return False
