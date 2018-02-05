"""
  Contains functions for calculating the distance
  between two locations with the Haversine Formula and
  the approx. amount of time it would take a plane to fly
  the distance.

"""

import math
from src.google_utils import get_geocode


def _kMtoUSNauticalMiles(num):
    return num / 1.852


def _deg2rad(deg):
    return deg * (math.pi / 180)


def _getDistanceFromLatLonInMeters(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = _deg2rad(lat2 - lat1)  # deg2rad below
    dLon = _deg2rad(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(_deg2rad(lat1)) * \
        math.cos(_deg2rad(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_in_km = R * c  # Distance in km
    distance_in_m = int(distance_in_km) * 1000
    return distance_in_m


def get_flight_duration_in_secs(distance_in_m):
    """
      Takes is the distance in meters and
      calculates the approx duration of a flight in secs
      assuming an average cruising speed is 878 km/h
      (approx. 224 m/s).

      :type distance: int
      :rtype: int
    """
    approx_mps = 224
    duration_in_secs = distance_in_m / approx_mps
    return duration_in_secs


def get_flight_distance_in_meters(origin, dest):
    origin = get_geocode(origin)
    dest = get_geocode(dest)
    lon1 = origin.get('lng', None)
    lon2 = dest.get('lng', None)
    lat1 = origin.get('lng', None)
    lat2 = dest.get('lng', None)

    R = 3440
    dInKm = _getDistanceFromLatLonInMeters(lat1, lon1, lat2, lon2)
    return dInKm
