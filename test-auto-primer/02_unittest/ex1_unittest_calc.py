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
from faulty_calc import Calc


class CalcTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.calc = Calc()

    @classmethod
    def tearDown(self):
        self.calc.reset()

    def test1(self):
        self.calc.start(5)
        output = self.calc.add(4)
        self.assertEqual(output, 9, "Wrong Calculation.")

    def test2(self):
        self.calc.start(5)
        self.calc.add(3)
        output = self.calc.add(4)
        self.assertEqual(output, 12, "Wrong Calculation.")

    def test3(self):
        self.calc.start(5)
        self.calc.sub(3)
        output = self.calc.sub(1)
        self.assertEqual(output, 1, "Wrong Calculation.")

    def test4(self):
        self.calc.start(5)
        output = self.calc.add(4)
        with self.assertRaises(Exception) as cm:
            self.calc.complain()
        self.assertIn("Expected", str(cm.exception))

    def test5(self):
        self.calc.start(5)
        output = self.calc.add(4)
        self.calc.why_complain()

unittest.main()