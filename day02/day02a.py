## Advent of code 2019, AoC day 2 puzzle 1
## This solution (python3.7) by kannix68, @ 2019-12-11.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc

import logging
logging.basicConfig(stream=sys.stdout, level=logging.WARN)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

## PROBLEM DOMAIN code

class IntcodeInterpreter:
  INITIALIZED = 0
  RUNNING = 1
  HALTED = 99

  def __init__(self, mem):
    self.mem = mem
    self.mem0 = mem.copy()
    self.ptr = 0  # instruction pointer
    self.ctr = 0  # instruction counter
    self.state = self.INITIALIZED
    print(f"initialized {self}")

  def __repr__(self):
    return "IntcodeInterpreter"

  def __str__(self):
    return f"IntcodeInterpreter ptr={self.ptr}, ctr={self.ctr}, state={self.state} mem={self.mem}"

  def step_program(self) -> None:
    """Interpret the program given in the puzzle (1 step). list in, list out."""
    mem = self.mem
    ptr = self.ptr
    #print(f"to-step {self}")
    opcode = mem[ptr]
    if opcode == 1:
      op1 = mem[ptr+1]
      op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = mem[op1] + mem[op2]
      self.ptr += 4
    elif opcode == 2:
      op1 = mem[ptr+1]
      op2 = mem[ptr+2]
      trg = mem[ptr+3]
      mem[trg] = mem[op1] * mem[op2]
      self.ptr += 4
    elif opcode == 99:
      self.state = self.HALTED
    else:
      raise(RuntimeError(f"illegal opcode {opcode}")) 
    self.ctr += 1
    print(f"stepped! {self}")

  def interpret_program(self) -> None:
    """Interpret the program given in the puzzle (all steps until prg-exit). list in, list out."""
    self.state = self.RUNNING
    while self.state != self.HALTED:
      self.step_program()
    print(f"interpreted halted! {self}")

def solve(inputs: list) -> list:
  computer = IntcodeInterpreter(inputs)
  computer.interpret_program()
  return computer.mem

## MAIN

### tests
ins = [1,9,10,3,2,3,11,0,99,30,40,50]
computer = IntcodeInterpreter(ins)
#result = solve(ins)
computer.interpret_program()
result = computer.mem
expectd = [3500,9,10,70,2,3,11,0,99,30,40,50]
aoc.assert_msg(f"input={ins} expects output={expectd}, got {result}", expectd == result)

ins = [1,0,0,0,99]
expectd = [2,0,0,0,99]
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {result}", expectd == result)

ins = [2,3,0,3,99]
expectd = [2,3,0,6,99]
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {result}", expectd == result)

ins = [2,4,4,5,99,0]
expectd = [2,4,4,5,99,9801]
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {result}", expectd == result)

ins = [1,1,1,4,99,5,6,0,99]
expectd = [30,1,1,4,2,5,6,0,99]
result = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {result}", expectd == result)

### personal input
data = aoc.read_file_firstline_to_str('day02.in')
data = list(map(int, data.split(',')))
data[1] = 12
data[2] = 2
print(f"data-type={type(data)} data={data}")

### personal solution
outputs = solve(data)

print(f"output={outputs}")
print(f"result={outputs[0]}")
