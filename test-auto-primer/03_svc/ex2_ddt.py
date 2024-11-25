# This file is a part of Arjuna-Workshops
# Copyright 2015-2021 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import requests
from ddt import ddt, data, unpack
from jsonschema import validate, ValidationError

@ddt
class TestJSONPlaceholderPOSTAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"
    POST_SCHEMA = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    @data(
        ({"title": "foo", "body": "bar", "userId": 1}, 201, True),  # Valid data
        ({"body": "bar", "userId": 1}, 400, False),                # Missing title
        ({"title": "foo", "userId": 1}, 400, False),               # Missing body
        ({"title": "foo", "body": "bar", "userId": "invalid"}, 400, False),  # Invalid userId type
        ({}, 400, False)                                           # Empty payload
    )
    @unpack
    def test_create_post(self, payload, expected_status, should_validate_schema):
        """Test POST /posts endpoint with various payloads."""
        # Make the POST request
        response = requests.post(self.BASE_URL, json=payload)

        # Assert the HTTP status code
        self.assertEqual(
            response.status_code,
            expected_status,
            f"Failed for payload: {payload}. Response: {response.text}"
        )

        # Validate schema if required and response is successful
        if should_validate_schema and response.status_code == 201:
            try:
                validate(instance=response.json(), schema=self.POST_SCHEMA)
            except ValidationError as e:
                self.fail(f"Schema validation failed for payload: {payload}. Error: {e}")

        # Verify the response content matches input payload for successful requests
        if response.status_code == 201:
            response_data = response.json()
            for key, value in payload.items():
                self.assertEqual(
                    response_data.get(key),
                    value,
                    f"Key '{key}' mismatch in payload: {payload}"
                )


if __name__ == "__main__":
    unittest.main(verbosity=5)
