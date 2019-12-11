## Advent of code 2019, AoC day 1 puzzle 1
## This solution (python3.7) by kannix68, @ 2019-12-11.

### generic aoc code
def assert_msg(msg, assertion):
  assert assertion, "ERROR on assert: {}".format(msg)
  print("assert-OK: {}".format(msg))

def expect_msg(msg, expected, inputs):
  assert_msg(msg.format(inputs, expected), expected == solve(inputs))

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

### problem domain code
def solve(input):
  return int(input/3)-2

## MAIN

### tests
expect_msg("input={} expects output={}", 2, 12)
expect_msg("input={} expects output={}", 2, 14)
expect_msg("input={} expects output={}", 654, 1969)
expect_msg("input={} expects output={}", 33583, 100756)

### personal input
data = read_file_to_list('day01.in')

### personal solution
print(f"input # of elements={len(data)}")
outputs = sum(map(solve, map(int, data)))

print(f"output={outputs}")
