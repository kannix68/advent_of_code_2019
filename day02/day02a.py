## Advent of code 2019, AoC day 2 puzzle 1
## This solution (python3.7) by kannix68, @ 2019-12-11.

#import itertools as itertools
import sys as sys

### generic aoc code
def assert_msg(msg, assertion):
  assert assertion, "ERROR on assert: {}".format(msg)
  print("assert-OK: {}".format(msg))

def expect_msg(msg, expected, inputs):
  """Assert an expected function result according to inputs."""
  results = solve(inputs)
  assert_msg(msg.format(inputs, expected, results), expected == results)

def read_file_to_str(filename):
  """Read a file into one string."""
  with open(filename, 'r') as inputfile:
    data = inputfile.read()
  return data

def read_file_firstline_to_str(filename):
  """Read the first line of a file into strings, each ending whitespace stripped."""
  with open(filename, 'r') as inputfile:
    line = inputfile.readline().rstrip()
  return line

def read_file_to_list(filename):
  """Read a file into a list of strings (per line), each ending whitespace stripped."""
  with open(filename, 'r') as inputfile:
    lines_list = inputfile.readlines()
  #lines_list = [line.rstrip('\n') for line in lines_list] # via list comprehension
  lines_list = list(map(lambda it: it.rstrip(), lines_list)) # via map
  return lines_list

## PROBLEM DOMAIN code

def step_program(pos, mem):
  """Interpret the program given in the puzzle (1 step). list in, list out."""
  assert(isinstance(pos, int), "check for input 1 type int")
  assert(isinstance(mem, list), "check for input 2 type list")
  print(f"to-step mem={mem}")
  opcode = mem[pos]
  if opcode == 1:
    op1 = mem[pos+1]
    op2 = mem[pos+2]
    trg = mem[pos+3]
    mem[trg] = mem[op1] + mem[op2]
  elif opcode == 2:
    op1 = mem[pos+1]
    op2 = mem[pos+2]
    trg = mem[pos+3]
    mem[trg] = mem[op1] * mem[op2]
  elif opcode == 99:
    return None # end-of-program
  else:
    raise(RuntimeError(f"illegal opcode {opcode}")) 
  print(f"stepped! mem={mem}")
  return mem

def interpret_program(mem):
  """Interpret the program given in the puzzle (all steps until prg-exit). list in, list out."""
  assert(isinstance(mem, list), "check for input type list")
  ct = 0
  pos = 0
  inmem = mem
  while True:
    ct += 1
    tmplst = step_program(pos, inmem)
    if tmplst is None:
      break
    inmem = tmplst
    pos += 4
  print(f"program execution counter={ct}")
  return inmem

def solve(inputs):
  assert_msg(f"check for input type list. inputs={inputs}", isinstance(inputs, list))
  outmem = interpret_program(inputs)
  return outmem

## MAIN

### tests
inlist = [1,9,10,3,2,3,11,0,99,30,40,50]
expectedlist = [3500,9,10,70,2,3,11,0,99,30,40,50]
expect_msg("input={} expects output={}; was={}", expectedlist, inlist)

inlist = [1,0,0,0,99]
expectedlist = [2,0,0,0,99]
expect_msg("input={} expects output={}; was={}", expectedlist, inlist)

inlist = [2,3,0,3,99]
expectedlist = [2,3,0,6,99]
expect_msg("input={} expects output={}; was={}", expectedlist, inlist)

inlist = [2,4,4,5,99,0]
expectedlist = [2,4,4,5,99,9801]
expect_msg("input={} expects output={}; was={}", expectedlist, inlist)

inlist = [1,1,1,4,99,5,6,0,99]
expectedlist = [30,1,1,4,2,5,6,0,99]
expect_msg("input={} expects output={}; was={}", expectedlist, inlist)

### personal input
data = read_file_firstline_to_str('day02.in')
data = list(map(int, data.split(',')))
data[1] = 12
data[2] = 2
print(f"data-type={type(data)} data={data}")

### personal solution
outputs = solve(data)

print(f"output={outputs}")
print(f"result={outputs[0]}")
