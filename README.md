# Kruxpy
[![Build Status](https://secure.travis-ci.org/theatlantic/kruxpy.png?branch=master)](https://travis-ci.org/theatlantic/kruxpy)

A python library for working with the [Salesforce DMP API](https://konsole.zendesk.com/hc/en-us/articles/216119137-Salesforce-DMP-API).  You will need an API Key - which your Salesforce DMP Solutions Representative will have to provide.


## Example Usage
```python
from kruxpy import Client

c = Client('username', 'password', 'apikey')

# This will return all 1st/3rd party segments
print(c.audiences)

# returns a list of sites
print(c.sites)

# get a list of segment overlaps for a given segment
print(c.get_audience_distribution('12345'))

# get a list of events
print(c.events)
```

## Logging
This library uses the standard [Python logging library](https://docs.python.org/3/library/logging.html).  To see debut output printed to STDOUT, for instance, use:

```python
import logging

log = logging.getLogger('kruxpy')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
```

## Running Tests
To run tests:

```
pip install -r dev-requirements.txt
python -m unittest
```
