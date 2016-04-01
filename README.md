# jupyterhub-urlauthenticator

Authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows all user logins against a url that returns a response indicating
if the login should succeed. If the response from the URL POST includes the
same `username` as in the `data` coming to the authenticator.authenticate
method, the login should succeed.

## Usage
After installation, you can then use the authenticator by adding the following
lines to your `jupyterhub_config.py` (replacing square bracket items with your
values):

```
c.JupyterHub.authenticator_class = 'urlauthenticator.UrlAuthenticator'
c.UrlAuthenticator.server_address = 'http://[address]'
c.UrlAuthenticator.server_port = [port]
c.UrlAuthenticator.login_route = '[/path/to/login/service]'
```

## Installation
```
pip install [-e] git+git://github.com/theaffiend/jupyterhub-urlauthenticator.git
```

It has no additional dependencies beyond JupyterHub (tornado is installed by
jupyterhub).

## TODO
* get this on pypi
* tests
* better code/auto doc

## Other
