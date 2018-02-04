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
    self.assertEqual(dist, 8278268)
    self.assertEqual(time, 275693)

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
    self.assertEqual(dist, 11193000)
    self.assertEqual(time, 49968)

  def test_flight_driving_combo(self):
    """
      If some parts can be driven and others can't,
      it should only calculate flight where it cant'.
    """
    locations = ['Portland+MA', 'Phoinex+AZ', 'Johannesburg']
    ret = get_most_efficient_route(locations)

    dist = ret.get('distance')
    time = ret.get('time')
    
    portland_to_phoenix_dist = 4399595
    phoenix_to_johannesburg_dist = 11193000
    self.assertEqual(dist, portland_to_phoenix_dist + phoenix_to_johannesburg_dist)
    
    portland_to_phoenix_time = 146001
    phoenix_to_johannesburg_time = 49968
    self.assertEqual(time, portland_to_phoenix_time + phoenix_to_johannesburg_time)

if __name__ == '__main__':
    unittest.main()