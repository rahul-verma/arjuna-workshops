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

# Just interacting
# What if it complains and you expected it to.

# Test 1
calc = Calc()
calc.start(5)
output = calc.add(4)
calc.complain() # Code exit
calc.reset()

# Test 2
calc = Calc()
calc.start(5)
calc.add(3)
output = calc.add(4)
calc.reset()