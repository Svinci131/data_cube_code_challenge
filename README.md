# Python Code Challenge

## NOTES:

In order to guarantee that this script is easily accessible, I decided to deploy via AWS Lambda. 

The number of calls allowed to the geocode api may be exceeded.

## Routes

POST - /route-calculator

## Expected Response

```
{
  "distance": "21639.268 km",
  "time": "3 days 21 hours 9 minutes 0 seconds"
}

```

## Example Requests

```

curl -d '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY"]}' \
-H "Content-Type: application/json" \
-X POST https://vezs8zsx61.execute-api.us-east-1.amazonaws.com/dev/route-calculator

```

or 

```

curl -d '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY", "Museum+Africa+Lilian+Ngoyi+St+Newtown+Johannesburg+2033+South+Africa"]}' \
-H "Content-Type: application/json" \
-X POST https://vezs8zsx61.execute-api.us-east-1.amazonaws.com/dev/route-calculator

```


## ASSUMPTIONS


  1. Locations will be given in formats the Google API can accept.

  2. If you can drive you must drive otherwise you must take a plane.

  3. We have a magic airplane that can take off without a runway and don't need to find the nearest airport.

  4. The plane will go at 878 km/h for the entire flight.

  5. Distance not time is what makes a route "efficient". So, it may take less time to fly from Paris to New York than to drive from Orlando from New York, but because there are fewer miles between Orlando from New York that's what counts toward efficiency.

  6. Distances are different in different directions.


## Develop - Run Locally
_Required: (PYTHON3)_
_(You will need to enter your own google maps API key.)_

```

cd [into_project]
virtualenv -p python3 .venv
source .venv/bin/activate
python -m src.main


```

^^ This will run an "example" invocation of the lambda handler without having to actually deploy. This is mainly to showcase how the app works.

## Develop - Run Tests

Decided to avoid using `pytest` since it would have been the only pip requirement for the app. To run tests (from dir root, assuming venv is activated),

```
python -m src.tests.test_route_calculator
```

## Python Code Challenge

Please write a Python server that:

Takes the addresses of 3 locations (valid addresses recognizable by the Google API ) outputs the distance and time taken of the most efficient route going through all 3 locations. No front end is necessary, the server may be queried via CURL with results being in a form of a JSON file. External APIs may be used for this assignment.

Bonus: allow to input an arbitrary number of locations as opposed to just 3.
