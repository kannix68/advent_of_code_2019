## Advent of code 2019, AoC day 2 puzzle 2
## This solution (python3.7) by kannix68, @ 2019-12-28.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc

import logging
logging.basicConfig(stream=sys.stdout, level=logging.WARN)
#log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)

## PROBLEM DOMAIN code
from intcode_interpreter import *

## MAIN

def solve(inputs: list) -> int:
  computer = IntcodeInterpreter(inputs)
  computer.interpret_program()
  return computer.mem[0]

### tests
ins = [1,9,10,3,2,3,11,0,99,30,40,50]
expected = 3500
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

ins = [1,0,0,0,99]
expected = 2
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

ins = [2,3,0,3,99]
expected = 2
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

ins = [2,4,4,5,99,0]
expected = 2
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

ins = [1,1,1,4,99,5,6,0,99]
expected = 30
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

### part 2 solution (given)
p2solution = 19690720

### personal input
data = aoc.read_file_firstline_to_str('day02.in')
data = list(map(int, data.split(',')))
print(f"data-type={type(data)} data={data}")

found = False
for noun in range(100):
  for verb in range(100):
    pdata = data.copy()
    pdata[1] = noun
    pdata[2] = verb
    # personal solution for this paramaterset
    out = solve(pdata)
    if out == 19690720:
      found = True
      print(f"solved: noun={noun}, verb={verb}, answer={100*noun+verb}")
      break
  if found:
    break
