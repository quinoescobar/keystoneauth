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

from keystoneauth1.identity.v3 import base

__all__ = ('RefreshTokenMethod', 'RefreshToken')

class RefreshTokenMethod(base.AuthMethod):
    """ """
    _method_parameters = ['client_id',
                          'client_secret',
                          'refresh_token']


    def get_auth_data(self, session, auth, headers, **kwargs):

        return

    def get_cache_id_elements(self):
        return dict(('refresh_token_%s' % p, getattr(self, p))
                    for p in self._method_parameters)



class RefreshToken(base.AuthConstructor):
    """ """

    _auth_method_class = RefreshTokenMethod
