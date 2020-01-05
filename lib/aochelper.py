##
# module aochelper
#
# Generic aoc code.
# Written for Advent of Code 2019
# by kannix68
# current as of 2020-01-04

from typing import Dict, List, Tuple


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

# from day 17a, reusable
# Input has already to be a list of strings (top-to-down).
def represent_strlist(strlist: List[str]) -> str:
  """Output a list-of-strings as aligned multiline string. Can be used for printing."""
  return "\n".join(strlist)

#
# Orientation is assumed top-to-bottom and left-to-right.
# Output is in order north, west, south, east.
def get_neighbors(strlist: List[str], x: int, y: int) -> List[str]:
  """Get a list of 4 neighbors of cell. May return '' as element if boundary."""
  max_y_idx = len(strlist) - 1
  max_x_idx = len(strlist[0]) - 1
  if x > 0:
    w = strlist[y][x-1]
  else:
    w = ''
  if x < max_x_idx:
    e = strlist[y][x+1]
  else:
    e = ''
  if y > 0:
    n = strlist[y-1][x]
  else:
    n = ''
  if y < max_y_idx:
    s = strlist[y+1][x]
  else:
    s = ''
  return [n, w, s, e]
