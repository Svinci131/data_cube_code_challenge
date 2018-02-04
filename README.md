## Python Code Challenge

### NOTES:

In order to guarentee that it was easily accessible I decided to deploy via AWS LAMBDA.

### Routes

POST - /route-calculator

#### Response Form

```
{
  distance: int, # meters
  time: int # seconds
}

```

#### Example Requests

```

curl -d '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY"]}' \
-H "Content-Type: application/json" \
-X POST https://vezs8zsx61.execute-api.us-east-1.amazonaws.com/dev/route-calculator

```

```

curl -d '{"locations": ["Portland+MA", "Phoinex+AZ", "New+York+NY", "Museum+Africa+Lilian+Ngoyi+St+Newtown+Johannesburg+2033+South+Africa"]}' \
-H "Content-Type: application/json" \
-X POST https://vezs8zsx61.execute-api.us-east-1.amazonaws.com/dev/route-calculator

```


### ASSUMPTIONS

  1. Order of locations matters. The first location is your origin, the last location is your final destination.
  _(So if given:
  [ Maine, Arizona, New York], you must go in order even though [ Maine, New York, Arizona] would be faster)._

  2. Locations will be given in forms the google api can accept.

  3. If you can drive you must drive otherwise you must take a plane.

  4. We have a magic airplane that can take off without a runway and don't need to find the nearest airport.

  5. The plane will go at 878 km/h for the entire flight.


## Develop - Run Locally
_Required: (PYTHON3)_
_(You will need to enter your own google maps API id.)_

```

cd [into_project]
virtualenv -p python3 .venv
source .venv/bin/activate
python -m src.main


```

### Python Code Challenge

Please write a Python server that:

Takes the addresses of 3 locations (valid addresses recognizable by the Google API ) outputs the distance and time taken of the most efficient route going through all 3 locations. No front end is necessary, the server may be queried via CURL with results being in a form of a JSON file. External APIs may be used for this assignment.

Bonus: allow to input an arbitrary number of locations as opposed to just 3.
