## Advent of code 2019, AoC day 3 puzzle 2
## This solution (python3.7) by kannix68, @ 2019-12-28.
#
# idea/algo for puzzle 2 stolen here:
#   https://github.com/matteobarbera/AdventOfCode2019/blob/master/Day3/day3_main.py
# my first attempt using networkx graph module and shortest_path had an error.

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

def get_positions(instr):
  is1 = instr.split(',')
  m1 = {} # list [], set, or as dict {} or dict()
  pos = [0,0]
  step = 0
  for instruct in is1:
    op = instruct[0]
    num = int(instruct[1:])
    for i in range(num):
      step += 1
      if op == 'R':
        pos[0] = pos[0] + 1
      elif op == 'L':
        pos[0] = pos[0] - 1
      elif op == 'U':
        pos[1] = pos[1] + 1
      elif op == 'D':
        pos[1] = pos[1] - 1
      else:
        raise(RuntimeError(f"illegal operation {op}"))
      tpos = tuple(pos)
      #m1.append(tuple(pos)) # tuples are hashable, lists are not
      if not tpos in m1:
        m1[tpos] = step
  return m1

def solve(inputs):
  lst1 = get_positions(inputs[0])
  lst2 = get_positions(inputs[1])
  reslt = set(lst1.keys()).intersection(set(lst2.keys())) # elements must be hashable
  print(f"intersections: {reslt}")
  dists = list(map(lambda pos: abs(pos[0]) + abs(pos[1]), reslt))
  print(f"distances: {dists}")
  m = min(dists)
  print(f"min-distance: {m}")
  cablenmin = 0
  for isect in reslt:
    cablen1 = lst1[isect]
    cablen2 = lst2[isect]
    cablensum = cablen1 + cablen2
    print(f"  isect={isect} cable-len: #1={cablen1}, #2={cablen2}, sum={cablensum}")
    if cablenmin > cablensum or cablenmin == 0:
      cablenmin = cablensum
      print(f"new min-path: {cablensum}")
  return cablenmin

## MAIN

### tests
ins = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
expectd = 30
res = solve(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

ins = ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']
expectd = 610
res = solve(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

ins = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
expectd = 410
res = solve(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

### personal input
data = read_file_to_list('day03.in')
res = solve(data)
print(f"solved: result min-shortest-bath={res}")

