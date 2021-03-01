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

from faulty_calc import Calc
from asserter import *

# Let's deal with pass/fail and exceptions.

calc = None

def setup():
    global calc
    calc = Calc()

def teardown():
    calc.reset()

def test1():
    calc.start(5)
    output = calc.add(4)
    assert_equals(output, 9, "Wrong Calculation.")

def test2():
    calc.start(5)
    calc.add(3)
    output = calc.add(4)
    assert_equals(output, 12, "Wrong Calculation.")

def test3():
    calc.start(5)
    calc.sub(3)
    output = calc.sub(1)
    assert_equals(output, 1, "Wrong Calculation.")

def test4():
    calc.start(5)
    output = calc.add(4)
    assert_exc(calc.complain, "Expected", "Calc did not complain properly.")

def test5():
    calc.start(5)
    output = calc.add(4)
    calc.why_complain() # Code exit


# Find all functions that start with the word test
all_tests = [n for n in globals() if n.startswith("test")]

for test in all_tests:
    # Dynamically call test function
    tfunc = globals()[test]
    try:
        setup() # This itself will have try/except/else block in practice
        tfunc()
        teardown() # This itself will have try/except/else block in practice
    except AssertionError as e:
        print("FAIL: {}".format(e))
    except Exception as f:
        print("ERROR: {}".format(f))
    else:
        print("PASS")