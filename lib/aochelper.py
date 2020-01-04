##
# module aochelper
#
# Generic aoc code.
# Written for Advent of Code 2019
# by kannix68
# current as of 2020-01-04

## file and i/o handling, messaging/logging
def assert_msg(msg: str, assertion) -> None:
  """Assert an expected function result according to inputs."""
  assert assertion, "ERROR on assert: {}".format(msg)
  print("assert-OK: {}".format(msg))

def expect_msg(msg: str, expected, inputs) -> None:
  """Assert an expected function result according to inputs."""
  results = solve(inputs)
  assert_msg(msg.format(inputs, expected, results), expected == results)

def read_file_to_str(filename: str) -> str:
  """Read a file into one string."""
  with open(filename, 'r') as inputfile:
    data = inputfile.read()
  return data

def read_file_firstline_to_str(filename: str) -> str:
  """Read the first line of a file into strings, each ending whitespace stripped."""
  with open(filename, 'r') as inputfile:
    line = inputfile.readline().rstrip()
  return line

def read_file_to_list(filename: str) -> str:
  """Read a file into a list of strings (per line), each ending whitespace stripped."""
  with open(filename, 'r') as inputfile:
    lines_list = inputfile.readlines()
  #lines_list = [line.rstrip('\n') for line in lines_list] # via list comprehension
  lines_list = list(map(lambda it: it.rstrip(), lines_list)) # via map
  return lines_list

## algorithms and data structures

# flatten a list
# see [python - How to make a flat list out of list of lists? - Stack Overflow](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)
# flatten = lambda l: [item for sublist in l for item in sublist]
def flatten(l: list) -> list:
  """Flatten an arbitrary list-of-lists into one flat list."""
  return [item for sublist in l for item in sublist]

# This currently only works on flat lists:
def cl(l: list) -> str:
  """Return compact list representation as str."""
  return f"[{','.join(map(str,l))}]"

# from day 10a, reusable
# Input has already to be a contiuous left-to right top-to-down list-of-lists
def represent_2d_char_list(l: list) -> str:
  """Output a 2d character list as aligned multiline string. Can be used for printing."""
  row_num = 0
  repres = ""
  for rowlist in l:
    if row_num > 0:
      repres += "\n"
    for c in rowlist:
      repres += str(c)
    row_num += 1
  return repres