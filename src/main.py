"""

 Main function handler.

"""

import logging
import json
from src.route_calculator import get_most_efficient_route

logger = logging.getLogger()
logger.setLevel(logging.INFO)

resp_headers = {
  'Content-Type': 'application/json'
}

def _response_wrapper(statusCode, body):
  return {
    'headers':resp_headers,
    'statusCode': statusCode,
    'body': body,
  } 

def handler(event, context):
  try:
    body = json.loads(event.get('body', '{}'))
    locations = body.get('locations', [])
    resp = get_most_efficient_route(locations)

    print ('RES', resp)
    return _response_wrapper(200, json.dumps(resp))
  except Exception as e:
    print('ERROR', str(e))
    return _response_wrapper(400, str(e))

if __name__ == '__main__':
  # example
  handler({'body': '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY", "Museum+Africa+Lilian+Ngoyi+St+Newtown+Johannesburg+2033+South+Africa"]}'}, {})