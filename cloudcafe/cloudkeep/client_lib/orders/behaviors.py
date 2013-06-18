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
from datetime import datetime, timedelta


class ClientLibOrdersBehaviors(object):
    def __init__(self, client, client_lib, config):
        self.client = client
        self.client_lib = client_lib
        self.config = config

        self.created_orders = []

    def get_tomorrow_timestamp(self):
        tomorrow = (datetime.today() + timedelta(days=1))
        return tomorrow.isoformat()

    def create_order_from_config(self, use_expiration=False,
                                  use_plain_text=True):
        expiration = None
        if use_expiration:
            expiration = self.get_tomorrow_timestamp()

        order = self.client_lib.create_order(
            name=self.config.name,
            expiration=expiration,
            algorithm=self.config.algorithm,
            bit_length=self.config.bit_length,
            cypher_type=self.config.cypher_type,
            mime_type=self.config.mime_type)
        return order

    def create_and_check_order(self, name=None, expiration=None,
                                algorithm=None, bit_length=None,
                                cypher_type=None, mime_type=None):
        order = self.create_order_overriding_cfg(
            name=name, expiration=expiration,
            algorithm=algorithm, bit_length=bit_length,
            cypher_type=cypher_type, mime_type=mime_type)
        resp = self.client.get_order(order.id)
        return {
            'order': order,
            'get_resp': resp
        }

    def create_order_from_config(self, use_expiration=True):
        expiration = None
        if use_expiration:
            expiration = self.get_tomorrow_timestamp()

        order = self.client_lib.create_order(
            name=self.config.name,
            expiration=expiration,
            algorithm=self.config.algorithm,
            bit_length=self.config.bit_length,
            cypher_type=self.config.cypher_type,
            mime_type=self.config.mime_type)
        return order

    def create_order_overriding_cfg(self, name=None, expiration=None,
                                     algorithm=None, bit_length=None,
                                     cypher_type=None, mime_type=None):
        """
        Allows for testing individual parameters on creation.
        """
        if name is None:
            name = self.config.name
        if algorithm is None:
            algorithm = self.config.algorithm
        if bit_length is None:
            bit_length = self.config.bit_length
        if cypher_type is None:
            cypher_type = self.config.cypher_type
        if mime_type is None:
            mime_type = self.config.mime_type

        order = self.client_lib.create_order(
            name=name,
            expiration=expiration,
            algorithm=algorithm,
            bit_length=bit_length,
            cypher_type=cypher_type,
            mime_type=mime_type)
        return order

    def delete_order(self, order_id, delete_secret=True):
        if delete_secret:
            order = self.client.get_order(order_id).entity
            if order is not None:
                secret_href = order.secret_href
                secret_id = self.get_id_from_ref(secret_href)
                self.secrets_client.delete_secret(secret_id)

        resp = self.client.delete_order(order_id)
        if order_id in self.created_orders:
            self.created_orders.remove(order_id)
        return resp

    def delete_all_created_orders_and_secrets(self):
        for order_id in self.created_orders:
            self.delete_order(order_id, delete_secret=True)

        self.created_orders = []
