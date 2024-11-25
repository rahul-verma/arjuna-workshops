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

class Calc:

    def __init__(self):
        self.__state = 0

    def start(self, num):
        self.__state += num

    def add(self, num):
        self.__state += num
        return self.__state

    def sub(self, num):
        return self.__state - num # Subsequent operations return wrong calculation as state was not updated.

    def reset(self):
        self.__state = 0

    def complain(self):
        raise Exception("Expected Complaint.")

    def why_complain(self):
        raise Exception("Unexpected Complaint.")
