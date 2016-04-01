from jupyterhub.auth import Authenticator

from tornado import gen


class UrlAuthenticator(Authenticator):
    """
    """

    @gen.coroutine
    def authenticate(self, handler, data):
        """
        Return the username if the authentication passes, None otherwise.
        """
        # TODO: this lets anyone through. change to actually authenticate!
        return data['username']
