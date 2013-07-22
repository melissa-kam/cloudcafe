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

from cafe.engine.models.behavior_response import BehaviorResponse


class CloudkeepResponse(BehaviorResponse):

    def __init__(self, resp):
        super(CloudkeepResponse, self).__init__()
        self.response = resp
        self.ref = None
        self.id = None
        self.status_code = None
        if resp is not None:
            self.ref = resp.entity.reference
            self.status_code = resp.status_code
        if self.ref is not None:
            self.id = resp.entity.get_id()


class CreateAndGetResponse(BehaviorResponse):

    def __init__(self, create_resp, get_resp):
        super(CreateAndGetResponse, self).__init__()
        self.create_resp = create_resp
        self.get_resp = get_resp
        self.ref = None
        self.id = None
        if create_resp is not None:
            self.ref = create_resp.ref
            self.id = create_resp.id
            self.create_status_code = create_resp.status_code
        if get_resp is not None:
            self.get_status_code = get_resp.status_code
