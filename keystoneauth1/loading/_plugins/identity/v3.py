# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystoneauth1 import exceptions
from keystoneauth1 import identity
from keystoneauth1 import loading


def _add_common_identity_options(options):
    options.extend([
        loading.Opt('user-id', help='User ID'),
        loading.Opt('username',
                    help='Username',
                    deprecated=[loading.Opt('user-name')]),
        loading.Opt('user-domain-id', help="User's domain id"),
        loading.Opt('user-domain-name', help="User's domain name"),
    ])


def _assert_identity_options(options):
    if (options.get('username') and
            not (options.get('user_domain_name') or
                 options.get('user_domain_id'))):
        m = "You have provided a username. In the V3 identity API a " \
            "username is only unique within a domain so you must " \
            "also provide either a user_domain_id or user_domain_name."
        raise exceptions.OptionError(m)


class Password(loading.BaseV3Loader):

    @property
    def plugin_class(self):
        return identity.V3Password

    def get_options(self):
        options = super(Password, self).get_options()
        _add_common_identity_options(options)

        options.extend([
            loading.Opt('password',
                        secret=True,
                        prompt='Password: ',
                        help="User's password"),
        ])

        return options

    def load_from_options(self, **kwargs):
        _assert_identity_options(kwargs)

        return super(Password, self).load_from_options(**kwargs)


class Token(loading.BaseV3Loader):

    @property
    def plugin_class(self):
        return identity.V3Token

    def get_options(self):
        options = super(Token, self).get_options()

        options.extend([
            loading.Opt('token',
                        secret=True,
                        help='Token to authenticate with'),
        ])

        return options


class _OpenIDConnectBase(loading.BaseFederationLoader):

    def load_from_options(self, **kwargs):
        if not (kwargs.get('access_token_endpoint') or
                kwargs.get('discovery_endpoint')):
            m = ("You have to specify either an 'access-token-endpoint' or "
                 "a 'discovery-endpoint'.")
            raise exceptions.OptionError(m)

        return super(_OpenIDConnectBase, self).load_from_options(**kwargs)

    def get_options(self):
        options = super(_OpenIDConnectBase, self).get_options()

        options.extend([
            loading.Opt('client-id', help='OAuth 2.0 Client ID'),
            loading.Opt('client-secret', secret=True,
                        help='OAuth 2.0 Client Secret'),
            loading.Opt('openid-scope', default="openid profile",
                        dest="scope",
                        help='OpenID Connect scope that is requested from '
                             'authorization server. Note that the OpenID '
                             'Connect specification states that "openid" '
                             'must be always specified.'),
            loading.Opt('access-token-endpoint',
                        help='OpenID Connect Provider Token Endpoint. Note '
                        'that if a discovery document is being passed this '
                        'option will override the endpoint provided by the '
                        'server in the discovery document.'),
            loading.Opt('discovery-endpoint',
                        help='OpenID Connect Discovery Document URL. '
                        'The discovery document will be used to obtain the '
                        'values of the access token endpoint and the '
                        'authentication endpoint. This URL should look like '
                        'https://idp.example.org/.well-known/'
                        'openid-configuration'),
            loading.Opt('access-token-type',
                        help='OAuth 2.0 Authorization Server Introspection '
                             'token type, it is used to decide which type '
                             'of token will be used when processing token '
                             'introspection. Valid values are: '
                             '"access_token" or "id_token"'),
        ])

        return options


class OpenIDConnectClientCredentials(_OpenIDConnectBase):

    @property
    def plugin_class(self):
        return identity.V3OidcClientCredentials

    def get_options(self):
        options = super(OpenIDConnectClientCredentials, self).get_options()

        return options


class OpenIDConnectPassword(_OpenIDConnectBase):

    @property
    def plugin_class(self):
        return identity.V3OidcPassword

    def get_options(self):
        options = super(OpenIDConnectPassword, self).get_options()

        options.extend([
            loading.Opt('username', help='Username', required=True),
            loading.Opt('password', secret=True,
                        help='Password', required=True),
        ])

        return options


class OpenIDConnectAuthorizationCode(_OpenIDConnectBase):

    @property
    def plugin_class(self):
        return identity.V3OidcAuthorizationCode

    def get_options(self):
        options = super(OpenIDConnectAuthorizationCode, self).get_options()

        options.extend([
            loading.Opt('redirect-uri', help='OpenID Connect Redirect URL'),
            loading.Opt('code', secret=True, required=True,
                        deprecated=[loading.Opt('authorization-code')],
                        help='OAuth 2.0 Authorization Code'),
        ])

        return options


class OpenIDConnectAccessToken(loading.BaseFederationLoader):

    @property
    def plugin_class(self):
        return identity.V3OidcAccessToken

    def get_options(self):
        options = super(OpenIDConnectAccessToken, self).get_options()

        options.extend([
            loading.Opt('access-token', secret=True, required=True,
                        help='OAuth 2.0 Access Token'),
        ])
        return options


class TOTP(loading.BaseV3Loader):

    @property
    def plugin_class(self):
        return identity.V3TOTP

    def get_options(self):
        options = super(TOTP, self).get_options()
        _add_common_identity_options(options)

        options.extend([
            loading.Opt('passcode', secret=True, help="User's TOTP passcode"),
        ])

        return options

    def load_from_options(self, **kwargs):
        _assert_identity_options(kwargs)

        return super(TOTP, self).load_from_options(**kwargs)


class TokenlessAuth(loading.BaseLoader):

    @property
    def plugin_class(self):
        return identity.V3TokenlessAuth

    def get_options(self):
        options = super(TokenlessAuth, self).get_options()

        options.extend([
            loading.Opt('auth-url', required=True,
                        help='Authentication URL'),
            loading.Opt('domain-id', help='Domain ID to scope to'),
            loading.Opt('domain-name', help='Domain name to scope to'),
            loading.Opt('project-id', help='Project ID to scope to'),
            loading.Opt('project-name', help='Project name to scope to'),
            loading.Opt('project-domain-id',
                        help='Domain ID containing project'),
            loading.Opt('project-domain-name',
                        help='Domain name containing project'),
        ])

        return options

    def load_from_options(self, **kwargs):
        if (not kwargs.get('domain_id') and
                not kwargs.get('domain_name') and
                not kwargs.get('project_id') and
                not kwargs.get('project_name') or
                (kwargs.get('project_name') and
                    not (kwargs.get('project_domain_name') or
                         kwargs.get('project_domain_id')))):
            m = ('You need to provide either a domain_name, domain_id, '
                 'project_id or project_name. '
                 'If you have provided a project_name, in the V3 identity '
                 'API a project_name is only unique within a domain so '
                 'you must also provide either a project_domain_id or '
                 'project_domain_name.')
            raise exceptions.OptionError(m)

        return super(TokenlessAuth, self).load_from_options(**kwargs)

class RefreshToken(loading.BaseV3Loader):
    """docstring for RefreshToken."""

    @property
    def plugin_class(self):
        return identity.V3RefreshToken


    def get_options(self):
        options = super(RefreshToken, self).get_options()

        options.extend([
            loading.Opt('client_id', require=True, help='Clien`s ID'),
            loading.Opt('client_secret', secret=True, require=True, help='Client`s Secret'),
            loading.Opt('refresh_token', require=True, help='User`s refresh token),
        ])

        return options


    def load_from_options(self, **kwargs):
        if (not kwargs.get('client_id') and
            not kwargs.get('client_secret') and
            not kwargs.get('refresh_token')):
            m = ('You need to provide the client_id,'
            'client_secret and the refresh_token.')
            raise exceptions.OptionError(m)

        return super(RefreshToken, self).load_from_options(**kwargs)
