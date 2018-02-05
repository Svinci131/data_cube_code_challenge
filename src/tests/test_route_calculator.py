import unittest
from src.route_calculator import get_most_efficient_route


class TestRouteCalculator(unittest.TestCase):

    def test_driving(self):
        """
          If driving is a viable option it should
          calculate combined distance and time of driving
          on roads.
        """
        locations = ['Portland+MA', 'Phoinex+AZ', 'New+York+NY']
        ret = get_most_efficient_route(locations)

        dist = ret.get('distance')
        time = ret.get('time')
        self.assertEqual(dist, '8278.268 km')
        self.assertEqual(time, '3 days 4 hours 34 minutes 53 seconds')

    def test_flight(self):
        """
          If driving is a viable option it should
          calculate distance and time flying at
          878 km/h.
        """
        locations = ['Phoinex+AZ', 'Johannesburg']
        ret = get_most_efficient_route(locations)

        dist = ret.get('distance')
        time = ret.get('time')
        self.assertEqual(dist, '11168.0 km')
        self.assertEqual(time, '0 days 13 hours 50 minutes 57 seconds')

    def test_flight_driving_combo(self):
        """
          If some parts can be driven and others can't,
          it should only calculate flight where it cant'.
        """
        locations = ['Portland+MA', 'Phoinex+AZ', 'Johannesburg']
        ret = get_most_efficient_route(locations)

        dist = ret.get('distance')
        time = ret.get('time')

        self.assertEqual(dist, '15567.595 km')
        self.assertEqual(time, '2 days 6 hours 24 minutes 18 seconds')


if __name__ == '__main__':
    unittest.main()
