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


def load_test_data(file_path):
    """Load test data from a tab-delimited file."""
    test_cases = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            row["Payload"] = json.loads(row["Payload"])
            row["SchemaValidation"] = row["SchemaValidation"].lower() == "true"
            test_cases.append(row)
    return test_cases


class DynamicAPITests(unittest.TestCase):
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

    def run_test_case(self, method, endpoint, payload, expected_status, schema_validation):
        """Execute a single API test case."""
        url = f"{self.BASE_URL}{endpoint}"

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

        # Assert schema validation if required
        if schema_validation and response.status_code in [200, 201]:
            try:
                validate(instance=response.json(), schema=self.POST_SCHEMA)
            except ValidationError as e:
                self.fail(f"Schema validation failed: {e}")

    @classmethod
    def generate_test_cases(cls):
        """Dynamically create test methods for each row in the test data."""
        test_data = load_test_data("test_data.tsv")

        for idx, test_case in enumerate(test_data):
            test_name = f"test_{test_case['TestName']}"

            def test_method(self, case=test_case):
                self.run_test_case(
                    method=case["Method"],
                    endpoint=case["Endpoint"],
                    payload=case["Payload"],
                    expected_status=int(case["ExpectedStatus"]),
                    schema_validation=case["SchemaValidation"]
                )

            setattr(cls, test_name, test_method)


# Dynamically generate test cases
DynamicAPITests.generate_test_cases()

if __name__ == "__main__":
    unittest.main(verbosity=5)
