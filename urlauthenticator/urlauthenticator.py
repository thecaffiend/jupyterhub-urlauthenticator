from jupyterhub.auth import Authenticator

from tornado import gen
from traitlets import (
    Unicode,
    Int,
)

import urllib, urllib.request
import json

class UrlAuthenticator(Authenticator):
    """
    Class for authenticating to jupyterhub against a remote URL.
    """

    # config values

    # address of the server hosting the login service
    server_address = Unicode(
        default_value='http://127.0.0.1',
        config=True,
        help='Address of the server with the login route'
    )

    # port the service is exposed on
    server_port = Int(
        default_value=8080,
        config=True,
        help='Port on which to contact login server',
    )

    # route to the service on the server_address:port
    # TODO: make this smarter about leading slashes...
    login_route = Unicode(
        default_value='/login',
        config=True,
        help='Route for the login service (assumes leading slash)'
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        """
        Authenticate against a URL that provisdes an authentication service.
        Args:
            handler - the RequestHandler from Jupyter
            data - the data from the hub login form.
        """
        url = '%s:%s%s' % (
            self.server_address,
            self.server_port,
            self.login_route
        )

        # get an httprequest with the headers and such using the provided data
        r = UrlAuthenticator.create_request(url, data)
        resp = None

        # hit the url and hopefully get a good response
        with urllib.request.urlopen(r) as f:
            resp = f.read()
            f.close()

        # if we had a good response, get the user name out of it (if there) and
        # return that. otherwise, return None (indicated bad login attempt)
        if resp is not None:
            d = json.loads(resp.decode())
            uname = d.get('username', None)
            return uname

        return None

    @staticmethod
    def create_request(url, data):
        """
        Make a Request object to hit the URL. Fills in some boilerplate stuff
        for a Request object.

        url is the full url (constructed from address, port, and route values)
        data is the data from a POST to the login form of the hub
        """
        r = None

        conttype = 'application/json; charset=UTF-8'
        jdata = json.dumps(data).encode('utf-8')

        headers = {
            'Content-Type': conttype,
            'Content-Length': len(jdata),
        }

        return urllib.request.Request(url, jdata, headers)
