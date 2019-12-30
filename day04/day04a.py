## Advent of code 2019, AoC day 4 puzzle 1
## This solution (python3.7) by kannix68, @ 2019-12-29.

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

def is_pw(innum):
  seq_found = False
  last_dig = -1
  for dig in map(int, str(innum)):
    if not seq_found and dig == last_dig:
      seq_found = True
    if dig < last_dig:
      return False
    last_dig = dig
  return seq_found

def solve(inputs):
  return is_pw(inputs)

## MAIN

### tests
ins = 111111
expectd = True
res = is_pw(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

ins = 223450
expectd = False
res = is_pw(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

ins = 123789
expectd = False
res = is_pw(ins)
assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)

### personal input solution

#Your puzzle input is 271973-785961.
start_num = 271973
end_num = 785961

pws_found = 0
for i in range(start_num, end_num+1):
  if is_pw(i):
    pws_found += 1

print(f"{pws_found} valid passwords found in range")

