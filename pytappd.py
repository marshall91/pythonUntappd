"""
pytappd.py - v0.1

Python wrapper for the Untappd API - https://untappd.com/api/docs

Author - Mackenzie Marshall <mackenziemarshall.com>
"""

import json
import urllib
import urllib2


class Untappd:
    def __init__(self, client_id, client_secret):
        self.url = 'http://api.untappd.com/v4/'
        self.client_id = client_id
        self.client_secret = client_secret

    def _do_get(self, method, params):
        url = self.url + method + "?client_id=" + self.client_id + "&client_secret=" + self.client_secret

        if params:
            params = urllib.urlencode(params)
            url = url + "&" + params
            response = urllib2.urlopen(url).read()
        else:
            response = urllib2.urlopen(url).read()

        return json.loads(response)

    def search(self, query):
        method = "search/beer"
        params = {
            "q": query
        }
        return self._do_get(method, params)


