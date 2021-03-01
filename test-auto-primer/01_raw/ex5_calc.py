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

# Let's deal with pass/fail and exceptions.

def test1():
    calc = Calc()
    calc.start(5)
    output = calc.add(4)
    calc.reset()
    if output != 9:
        raise AssertionError("Wrong calculation. Expected: {}. Got {}".format(9, output))
    calc.reset()

def test2():
    calc = Calc()
    calc.start(5)
    calc.add(3)
    output = calc.add(4)
    if output != 12:
        raise AssertionError("Wrong calculation. Expected: {}. Got {}".format(12, output))
    calc.reset()

def test3():
    calc = Calc()
    calc.start(5)
    calc.sub(3)
    output = calc.sub(1)
    if output != 1:
        raise AssertionError("Wrong calculation. Expected: {}. Got {}".format(1, output))
    calc.reset()

def test4():
    calc = Calc()
    calc.start(5)
    output = calc.add(4)
    try:
        calc.complain()
    except Exception:
        pass
    else:
        raise Exception("Expected exception not raised.")
    calc.reset()

def test5():
    calc = Calc()
    calc.start(5)
    output = calc.add(4)
    calc.why_complain() # Code exit
    calc.reset()


# Find all functions that start with the word test
all_tests = [n for n in globals() if n.startswith("test")]

for test in all_tests:
    # Dynamically call test function
    tfunc = globals()[test]
    try:
        tfunc()
    except AssertionError as e:
        print("FAIL: {}".format(e))
    except Exception as f:
        print("ERROR: {}".format(f))
    else:
        print("PASS")