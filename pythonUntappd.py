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
        self.url = 'https://api.untappd.com/v4/'
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

    def _get_access_token(self):
        """
        Internal function to return the authed users access token
        """
        return "access_token=" + self.auth

    def _do_get(self, method, auth, params):
        """
        Internal Function to send GETd requests

        Arguments:
            method = Untappd API method
            authorization = URL encoding of Untappd API authorization tokens
            params = Params for the API request
        """
        url = self.url + method + "?" + auth

        if params:
            params = urllib.urlencode(params)
            url = url + "&" + params
            response = urllib2.urlopen(url).read()
        else:
            response = urllib2.urlopen(url).read()

        return json.loads(response)

    def _do_post(self, method, auth, params):
        """
        Internal Function to send POST requests

        Arguments:
            method = Untappd API method
            authorization = URL encoding of Untappd API authorization tokens
            params = Params for the API request
        """
        url = self.url + method + "?" + auth
        params = urllib.urlencode(params)
        response = urllib2.urlopen(url, params).read()

        return json.loads(response)

    """
    Untappd API Feed Calls
    """
    def friend_feed(self, max_id=None, limit=None):
        """
        Returns the friends checkin feed

        Arguments:
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = 'checkin/recent'
        auth = self._get_access_token()
        params = {}
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    def user_feed(self, username, max_id=None, limit=None):
        """
        Returns the checkin feed of a specific user

        Arguments:
            username = the username of the user
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = 'user/checkin/' + username
        auth = self._get_api_auth_token()
        params = {}
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    def pub_feed(self, **kwargs):
        """
        Returns the checkin feed of around a location

        Arguments:
            min_id = the checkin id of the most recent checkin (optional)
            lng = the longitude of the public feed (optional)
            lat = the latitude of the public feed (optional)
            radius = the max radius the checkins start from (optional)
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = 'thepub/local'
        auth = self._get_api_auth_token()
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

        return self._do_get(method, auth, params)

    def venue_feed(self, venue_id, min_id=None, max_id=None, limit=None):
        """
        Returns the feed of a venue

        Arguments:
            venue_id = the id of the venue
            min_id = the checkin id of the most recent checkin (optional)
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = "venue/checkins/" + venue_id
        auth = self._get_api_auth_token()
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    def beer_feed(self, beer_id, min_id=None, max_id=None, limit=None):
        """
        Returns the feed of a beer

        Arguments:
            beer_id = the id of the beer
            min_id = the checkin id of the most recent checkin (optional)
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = "beer/checkins/" + beer_id
        auth = self._get_api_auth_token()
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    def brewery_feed(self, brewery_id, min_id=None, max_id=None, limit=None):
        """
        Returns the feed of a brewery

        Arguments:
            brewery_id = the id of the brewery
            min_id = the checkin id of the most recent checkin (optional)
            max_id = checkin id the results will start with (optional)
            limit = number of results to return (optional)
        """
        method = "brewery/checkins/" + brewery_id
        auth = self._get_api_auth_token()
        params = {}
        if min_id:
            params['min_id'] = min_id
        if max_id:
            params['max_id'] = max_id
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    """
    Untappd API Info Calls
    """
    def brewery_info(self, brewery_id, compact=None):
        """
        Returns the information of a brewery

        Arguments:
            brewery_id = the id of the brewery
            compact = pass "true" to return a compact listing of the brewery (optional)
        """
        method = "brewery/info/" + brewery_id
        auth = self._get_api_auth_token()
        params = {}
        if compact:
            params['compact'] = compact

        return self._do_get(method, auth, params)

    def beer_info(self, beer_id, compact=None):
        """
        Returns the information of a beer

        Arguments:
            beer_id = the id of the beer
            compact = pass "true" to return a compact listing of the beer (optional)
        """
        method = "beer/info/" + beer_id
        auth = self._get_api_auth_token()
        params = {}
        if compact:
            params['compact'] = compact

        return self._do_get(method, auth, params)

    def venue_info(self, venue_id, compact=None):
        """
        Returns the information of a venue

        Arguments:
            venue_id = the id of the venue
            compact = pass "true" to return a compact listing of the venue (optional)
        """
        method = "venue/info/" + venue_id
        auth = self._get_api_auth_token()
        params = {}
        if compact:
            params['compact'] = compact

        return self._do_get(method, auth, params)

    def checkin_info(self, checkin_id):
        """
        Returns the information of a checkin

        Arguments:
            checkin_id = the id of the checkin
        """
        method = "checkin/view/" + checkin_id
        auth = self._get_api_auth_token()

        return self._do_get(method, auth, {})

    def user_info(self, username, compact=None):
        """
        Returns the information of a user

        Arguments:
            user_id = the id of the user
            compact = pass "true" to return a compact listing of the user (optional)
        """
        method = "user/info/" + username
        auth = self._get_api_auth_token()
        params = {}
        if compact:
            params['compact'] = compact

        return self._do_get(method, auth, params)

    """
    Untappd API User Detail Calls
    """
    def user_badges(self, username, offset=None):
        """
        Returns a list of the users badges

        Arguments:
            username = the username of the user
            offset = the numeric offset where the results start (optional)
        """
        method = "user/badges/" + username
        auth = self._get_access_token()
        params = {}
        if offset:
            params['offset'] = offset

        return self._do_get(method, auth, params)

    def user_friends(self, username, offset=None, limit=None):
        """
        Returns a list of the users friends

        Arguments:
            username = the username of the user
            offset = the numeric offset where the results start (optional)
            limit = number of results to return (optional)
        """
        method = "user/friends/" + username
        auth = self._get_api_auth_token()
        params = {}
        if offset:
            params['offset'] = offset
        if limit:
            params['limit'] = limit

        return self._do_get(method, auth, params)

    def user_wishlist(self, username, sort=None, offset=None):
        """
        Returns a list of the users wishlisted beers

        Arguments:
            username = the username of the user
            sort = the value by which to sort the list (optional)
            offset = the numeric offset where the results start (optional)
        """
        method = "user/wishlist/" + username
        auth = self._get_api_auth_token()
        params = {}
        if sort:
            params['sort'] = sort
        if offset:
            params['offset'] = offset

        return self._do_get(method, auth, params)

    def user_distinct_beers(self, username, sort=None, offset=None):
        """
        Returns a list of the distinct beers a user has had

        Arguments:
            username = the username of a user
            sort = the value by which to sort the list (optional)
            offset = the numeric offset where the results start (optional)
        """
        method = "user/beers/" + username
        auth = self._get_api_auth_token()
        params = {}
        if sort:
            params['sort'] = sort
        if offset:
            params['offset'] = offset

        return self._do_get(method, auth, params)

    """
    Untappd API Search Calls
    """
    def brewery_search(self, query):
        """
        Returns the breweries matching a query

        Arguments:
            query = the search term to search by
        """
        method = "search/brewery"
        auth = self._get_api_auth_token()
        params = {
            "q": query
        }

        return self._do_get(method, auth, params)

    def beer_search(self, query, sort=None):
        """
        Returns the beer matching a query

        Arguments:
            query = the search term to search by
            sort = the value by which to sort the list (optional)
        """
        method = "search/beer"
        auth = self._get_api_auth_token()
        params = {
            "q": query
        }
        if sort:
            params['sort'] = sort
        return self._do_get(method, auth, params)

    def beer_trending(self):
        """
        Returns the trending macro and micro beers
        """
        method = "beer/trending"
        auth = self._get_api_auth_token()

        return self._do_get(method, auth, {})

    """
    Untappd API User Actions
    """
    def checkin(self, gmt_offset, timezone, beer_id, **kwargs):
        """
        Checks in a beer for a user

        Arguments:
            gmt_offset = the numeric offset the user is away from GMT
            timezone = the timezone of the user
            beer_id = the id of the beer the user is checking in
            foursquare_id = MD5 hash of the venue id (optional)
            geolat = the numeric latitude of the user, required if adding location (optional)
            geolng = the numeric longitude of the user, required if adding location (optional)
            shout = text to be added as a comment to the checkin (optional)
            rating = the numeric rating for the beer being checked in (optional)
            facebook = pass "on" to post the checkin to Facebook (optional)
            twitter = pass "on" to post the checkin to Twitter (optional)
            foursquare = pass "on" to post the checkin to Foursquare (optional)
        """
        method = "checkin/add"
        auth = self._get_access_token()
        params = {
            "gmt_offset": gmt_offset,
            "timezone": timezone,
            "bid": beer_id
        }
        if "foursquare_id" in kwargs:
            params['foursquare_id'] = kwargs['foursquare_id']
        if "geolat" in kwargs:
            params["geolat"] = kwargs["geolat"]
        if "geolng" in kwargs:
            params["geolng"] = kwargs["geolng"]
        if "shout" in kwargs:
            params["shout"] = kwargs["shout"]
        if "rating" in kwargs:
            params["rating"] = kwargs["rating"]
        if "facebook" in kwargs:
            params["facebook"] = kwargs["facebook"]
        if "twitter" in kwargs:
            params["twitter"] = kwargs["twitter"]
        if "foursquare" in kwargs:
            params["foursquare"] = kwargs["foursquare"]

        return self._do_post(method, auth, params)

    def add_comment(self, checkin_id, comment):
        """
        Adds a comment to a checkin

        Arguments:
            checkin_id = the id of the checkin to add a comment to
            comment = the text to add as a comment
        """
        method = "checkin/addcomment/" + checkin_id
        auth = self._get_access_token()
        params = {
            "comment": comment
        }

        return self._do_post(method, auth, params)

    def remove_comment(self, comment_id):
        """
        Removes a comment on a checkin

        Arguments:
            comment_id = the id of the comment to be removed
        """
        method = "checkin/deletecomment/" + comment_id
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    def toast(self, checkin_id):
        """
        Toggles the toast option on a checkin for a user

        Arguments:
            checkin_id = the id of the checkin to toggle the toast option
        """
        method = "checkin/toast/" + checkin_id
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    def add_to_wishlist(self, beer_id):
        """
        Adds a beer to a users wishlist

        Arguments:
            beer_id = the beer id of the beer to add to the wishlist
        """
        method = "user/wishlist/add"
        auth = self._get_access_token()
        params = {
            "bid": beer_id
        }

        return self._do_get(method, auth, params)

    def remove_from_wishlist(self, beer_id):
        """
        Removes a beer from a users wishlist

        Arguments:
            beer_id = the beer id of the beer to remove from the wishlist
        """
        method = "user/wishlist/delete"
        auth = self._get_access_token()
        params = {
            "bid": beer_id
        }

        return self._do_get(method, auth, params)

    """
    Untappd API Friends Calls
    """
    def pending_friends(self):
        """
        Returns a list of all the pending friend requests for a user
        """
        method = "user/pending"
        auth = self._get_access_token()

        return self._do_get(method, auth, {})

    def accept_friend(self, target_user):
        """
        Accepts the friend request for a user

        Arguments:
            target_user = the username of the friend request we are accepting
        """
        method = "friend/accept/" + target_user
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    def reject_friend(self, target_user):
        """
        Rejects the friend request for a user

        Arguments:
            target_user = the username of the friend request we are rejecting
        """
        method = "friend/reject/" + target_user
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    def remove_friend(self, target_user):
        """
        Removes a friend

        Arguments:
            target_user = the username of the friend request we are removing
        """
        method = "friend/remove/" + target_user
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    def request_friend(self, target_user):
        """
        Requests friendship to a user

        Arguments:
            target_user = the username of the friend request we are requesting
        """
        method = "friend/request/" + target_user
        auth = self._get_access_token()

        return self._do_post(method, auth, {})

    """
    Untappd API Misc Calls
    """
    def notifications(self):
        """
        Returns a list of notifications for a user
        """
        method = "notifications"
        auth = self._get_access_token()

        return self._do_get(method, auth, {})

    def foursquare_venue_lookup(self, venue_id):
        """
        Converts a Foursquare v2 ID in to a Untappd Venue ID

        Arguments:
            venue_id = the Foursquare v2 ID you wish to convert
        """
        method = "venue/foursquare_lookup/" + venue_id
        auth = self._get_api_auth_token()

        return self._do_get(method, auth, {})
