"""

 Main function handler.

"""

import json
import logging
from src.route_calculator import get_most_efficient_route

logger = logging.getLogger()
logger.setLevel(logging.INFO)

resp_headers = {'Content-Type': 'application/json'}


def _response_wrapper(statusCode, body):
    return {'headers': resp_headers, 'statusCode': statusCode,
            'body': body}


def handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        locations = body.get('locations', [])
        resp = get_most_efficient_route(locations)

        logger.info('RES', resp)
        return _response_wrapper(200, json.dumps(resp))
    except BaseException as e:
        logger.info('ERROR', str(e))
        return _response_wrapper(400, str(e))

'''
  Quick test run
  Protip: Don't forget to set a valid API Key!
'''
if __name__ == '__main__':
  # example
  handler({'body': '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY", "Museum+Africa+Lilian+Ngoyi+St+Newtown+Johannesburg+2033+South+Africa"]}'}, {})

