## Advent of code 2019, AoC day 1 puzzle 2
## This solution (python3.7) by kannix68, @ 2019-12-11.

import itertools as itertools

### generic aoc code
def assert_msg(msg, assertion):
  assert assertion, "ERROR on assert: {}".format(msg)
  print("assert-OK: {}".format(msg))

def expect_msg(msg, expected, inputs):
  results = solve(inputs)
  assert_msg(msg.format(inputs, expected, results), expected == results)

def read_file_to_str(filename):
  """Read a file into one string."""
  with open(filename, 'r') as inputfile:
    data = inputfile.read()
  return data

def read_file_to_list(filename):
  """Read a file into a list of strings (per line), each ending whitespace stripped."""
  with open(filename, 'r') as inputfile:
    lines_list = inputfile.readlines()
  #lines_list = [line.rstrip('\n') for line in lines_list] # via list comprehension
  lines_list = list(map(lambda it: it.rstrip(), lines_list)) # via map
  return lines_list

## PROBLEM DOMAIN code

def calc_fuel(inputs):
  """Calculate fuel for given mass."""
  return int(inputs/3)-2

def solve(inputs):
  """Solve the puzzle."""
  # functional:
  # define an infinite genrator for calc_fuel using yield
  # lst = itertools.takewhile(...)
  fuel = inputs
  fuel_sum = 0
  while True:
   fuel = calc_fuel(fuel)
   if fuel <= 0:
     break
   fuel_sum += fuel
  return fuel_sum

## MAIN

### tests
expect_msg("input={} expects output={}; was={}", 2, 14)
expect_msg("input={} expects output={}; was={}", 966, 1969)
expect_msg("input={} expects output={}; was={}", 50346, 100756)

### personal input
data = read_file_to_list('day01.in')

### personal solution
print(f"input # of elements={len(data)}")
outputs = sum(map(solve, map(int, data)))

print(f"output={outputs}")
