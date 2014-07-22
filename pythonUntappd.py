"""
pythonUntappd.py - v0.1

Python wrapper for the Untappd API - https://untappd.com/api/docs

Author - Mackenzie Marshall <mackenziemarshall.com>
"""

import json
import urllib
import urllib2


class api:
    """
    Arguments:
        client_id = Untappd API Client ID
        client_secret = Untappd API Client Secret
    """
    def __init__(self, client_id, client_secret):
        self.url = 'http://api.untappd.com/v4/'
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth = None
        self.user_auth_params = None

    def set_auth(self, auth):
        """
        Method to set the auth token for a request given by Untappd's API after user authorization

        Argument:
            auth = Untappd API access token
        """
        self.auth = auth

    def _get_api_auth_token(self):
        """
        Internal function to get the access token if set, of the client ID and secret
        """
        if self.auth:
            return "access_token=" + self.auth
        else:
            return "client_id=" + self.client_id + "&client_secret=" + self.client_secret

    def _do_get(self, method, params):
        """
        Internal Function to send GETd requests

        Arguments:
            method = Untappd API method
            authorization = URL encoding of Untappd API authorization tokens
            params = Params for the API request
        """
        url = self.url + method + "?" + self._get_api_auth_token()

        if params:
            params = urllib.urlencode(params)
            url = url + "&" + params
            response = urllib2.urlopen(url).read()
        else:
            response = urllib2.urlopen(url).read()

        return json.loads(response)

    def _do_post(self, method, params):
        """
        Internal Function to send POST requests

        Arguments:
            method = Untappd API method
            authorization = URL encoding of Untappd API authorization tokens
            params = Params for the API request
        """
        url = self.url + method + "?" + self._get_api_auth_token()
        params = urllib.urlencode(params)
        response = urllib2.urlopen(url, params).read()

        return json.loads(response)

    """
    Untappd API Feed Calls
    """
    def friend_feed(self, max_id=None, limit=None):
        method = 'checkin/recent'
        params = {}
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, params)

    def user_feed(self, username, max_id=None, limit=None):
        method = 'user/checkin/' + username
        params = {}
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, params)

    def pub_feed(self, **kwargs):
        method = 'thepub/local'
        params = {}
        if 'min_id' in kwargs:
            params['min_id'] = kwargs['min_id']
        if 'lng' in kwargs:
            params['lng'] = kwargs['lng']
        if 'lat' in kwargs:
            params['lat'] = kwargs['lat']
        if 'radius' in kwargs:
            params['radius'] = kwargs['radius']
        if 'max_id' in kwargs:
            params['max_id'] = kwargs['max_id']
        if 'limit' in kwargs:
            params['limit'] = kwargs['limit']

        return self._do_get(method, params)

    def venue_feed(self, venue_id, min_id=None, max_id=None, limit=None):
        method = "venue/checkins/" + venue_id
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, params)

    def beer_feed(self, beer_id, min_id=None, max_id=None, limit=None):
        method = "beer/checkins/" + beer_id
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, params)

    def brewery_feed(self, brewery_id, min_id=None, max_id=None, limit=None):
        method = "brewery/checkins/" + brewery_id
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, params)

    def beer_search(self, query, sort=None):
        method = "search/beer"
        params = {
            "q": query
        }
        if sort:
            params['sort'] = sort
        return self._do_get(method, params)


