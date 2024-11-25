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

def assert_equals(left, right, msg):
    if left != right:
        raise AssertionError("{} != {}. {}".format(left, right, msg))

def assert_exc(callable, exc_msg, msg):
    try:
        callable()
    except Exception as e:
        if exc_msg not in str(e):
            raise AssertionError("Expected exception msg not got. Expected: {}. Got: {}. {}.".format(exc_msg, str(e), msg))
