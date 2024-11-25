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
from jsonschema import validate, ValidationError

class TestJSONPlaceholderAPI(unittest.TestCase):
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

    def test_create_post(self):
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(self.BASE_URL, json=new_post)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data['title'], new_post['title'])
        self.assertEqual(response_data['body'], new_post['body'])
        self.assertEqual(response_data['userId'], new_post['userId'])
        self.assertIn('id', response_data)
        try:
            validate(instance=response_data, schema=self.POST_SCHEMA)
        except ValidationError as e:
            self.fail(f"Response schema validation failed: {e}")

    def test_read_post(self):
        post_id = 1
        response = requests.get(f"{self.BASE_URL}/{post_id}")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['id'], post_id)
        try:
            validate(instance=response_data, schema=self.POST_SCHEMA)
        except ValidationError as e:
            self.fail(f"Response schema validation failed: {e}")

    def test_update_post(self):
        post_id = 1
        updated_post = {
            "id": post_id,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        response = requests.put(f"{self.BASE_URL}/{post_id}", json=updated_post)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['title'], updated_post['title'])
        self.assertEqual(response_data['body'], updated_post['body'])
        self.assertEqual(response_data['userId'], updated_post['userId'])
        self.assertEqual(response_data['id'], updated_post['id'])
        try:
            validate(instance=response_data, schema=self.POST_SCHEMA)
        except ValidationError as e:
            self.fail(f"Response schema validation failed: {e}")

    def test_delete_post(self):
        post_id = 1
        response = requests.delete(f"{self.BASE_URL}/{post_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{}')

if __name__ == '__main__':
    unittest.main()
