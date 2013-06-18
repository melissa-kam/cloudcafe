"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from barbicanclient.client import Connection


class ClientLibSecretsClient():
    def __init__(self, url, api_version, tenant_id, auth_endpoint=None,
                 user=None, key=None, token=None, authenticate=None,
                 request=None, **kwargs):
        self.url = url
        self.api_version = api_version
        self.tenant_id = tenant_id
        endpoint = '{base}/{api_version}/{tenant_id}'.format(
            base=self.url, api_version=self.api_version,
            tenant_id=self.tenant_id)
        self.conn = Connection(
            endpoint=endpoint, auth_endpoint=auth_endpoint,
            user=user, key=key, tenant=tenant_id, token=token,
            authenticate=authenticate, request=request, **kwargs)

    def create_secret(self, name=None, expiration=None, algorithm=None,
                      bit_length=None, cypher_type=None, plain_text=None,
                      mime_type=None):
        secret = self.conn.create_secret(
            name=name, expiration=expiration, algorithm=algorithm,
            bit_length=bit_length, cypher_type=cypher_type,
            plain_text=plain_text, mime_type=mime_type)

        return secret

    def list_secrets(self):
        return self.conn.list_secrets()

    def delete_secret_by_id(self, secret_id):
        return self.conn.delete_secret_by_id(secret_id=secret_id)

    def delete_secret(self, href):
        return self.conn.delete_secret(href=href)

    def get_secret_by_id(self, secret_id):
        return self.conn.get_secret_by_id(secret_id=secret_id)

    def get_secret(self, href):
        return self.conn.get_secret(href=href)

    def get_raw_secret_by_id(self, secret_id, mime_type):
        return self.conn.get_raw_secret_by_id(
            secret_id=secret_id, mime_type=mime_type)

    def get_raw_secret(self, href, mime_type):
        return self.conn.get_raw_secret(href=href, mime_type=mime_type)
