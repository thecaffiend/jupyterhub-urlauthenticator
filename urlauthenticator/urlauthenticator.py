from jupyterhub.auth import Authenticator

from tornado import gen
from traitlets import (
    Unicode,
    Int,
)

class UrlAuthenticator(Authenticator):
    """
    """

    # address of the server hosting the login service
    server_address = Unicode(
        default_value='http://localhost',
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
        default_value='/api/login',
        config=True,
        help='Route for the login service (assumes leading slash)'
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        """
        Return the username if the authentication passes, None otherwise.
        """
        # TODO: this lets anyone through. change to actually authenticate!
        return data['username']
