pythonUntappd
=======

Python Library for Untappd API

Usage
------
Initialize api wrapper
```python
api = pythonUntappd.api("CLIENT_ID","CLIENT_SECRET")
```

Add access token from user
```python
api.set_auth("ACCESS_TOKEN")
```

Search for a beer
```python
api.beer_search("Blue Buck")
```

Full API documentation for Untappd can be found at:
[http://untappd.com/api/docs]