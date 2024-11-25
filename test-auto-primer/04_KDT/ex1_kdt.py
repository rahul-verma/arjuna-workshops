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
import json
import csv
from jsonschema import validate, ValidationError

class KeywordDrivenTest(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com"
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

    def setUp(self):
        """Read test data from the tab-delimited file."""
        self.test_data = []
        with open("test_data.tsv", "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                row["Payload"] = json.loads(row["Payload"])
                row["SchemaValidation"] = row["SchemaValidation"].lower() == "true"
                self.test_data.append(row)

    def execute_test(self, test_case):
        """Execute a single test case based on the test data."""
        method = test_case["Method"]
        url = f"{self.BASE_URL}{test_case['Endpoint']}"
        payload = test_case["Payload"]
        expected_status = int(test_case["ExpectedStatus"])
        schema_validation = test_case["SchemaValidation"]

        # Dispatch the appropriate HTTP method
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=payload)
        elif method == "PUT":
            response = requests.put(url, json=payload)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            self.fail(f"Unsupported HTTP method: {method}")

        # Assert status code
        self.assertEqual(response.status_code, expected_status)

        # Assert schema if required
        if schema_validation and response.status_code in [200, 201]:
            try:
                validate(instance=response.json(), schema=self.POST_SCHEMA)
            except ValidationError as e:
                self.fail(f"Schema validation failed: {e}")

    def test_keyword_driven(self):
        """Run all tests dynamically from the test data."""
        for test_case in self.test_data:
            with self.subTest(test_name=test_case["TestName"]):
                self.execute_test(test_case)

if __name__ == "__main__":
    unittest.main(verbosity=5)
