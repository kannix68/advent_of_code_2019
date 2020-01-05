#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 17 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-05.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


# In[ ]:


## PROBLEM DOMAIN code
from lib.intcode_interpreter import *


# In[ ]:


def get_mazelst_intersect_prodsum(maze_lst):
  result = 0
  for y in range(len(maze_lst)):
    for x in range(len(maze_lst[0])):
      if maze_lst[y][x] == '#': # crossings only if own cell is on a rail
        nbrs = aoc.get_neighbors(maze_lst, x, y)
        if ''.join(nbrs) == '####':
          log.info(f"intersection found at ({x,y})")
          result += x*y
  return result


# In[ ]:


def solve(program: list, base_combi: list) -> int:
  return 0


# In[ ]:


## MAIN


# In[ ]:


### tests
log.setLevel(logging.DEBUG)


# In[ ]:


# example "1"
maze_str = """
..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
""".strip()
maze_lst = maze_str.split("\n")
log.info(f"maze_lst=\n{aoc.represent_strlist(maze_lst)}")
result = get_mazelst_intersect_prodsum(maze_lst)
print(f"result={result}") 


# In[ ]:


### personal input solution, puzzle 1
log.setLevel(logging.INFO)
data = aoc.read_file_firstline_to_str('day17.in')
data = list(map(int, data.split(',')))
log.debug(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = IntcodeInterpreter(data, mem_growable=True)
computer.interpret_program()
outputs = computer.pseudo_stdout
log.debug(f"outputs={outputs}")
maze_str = ""
for i in outputs:
  if i < 32:
    if i == 10:
      maze_str += "\n"
    else:
      raise(RuntimeError(f"input ASCII non-printable char #{i} not handled")) 
  else:
    maze_str += chr(i)

maze_lst = maze_str.strip().split("\n")
#log.info(f"mazestr=\n{maze_str}")
log.info(f"maze_lst=\n{aoc.represent_strlist(maze_lst)}")
result = get_mazelst_intersect_prodsum(maze_lst)
print(f"result={result}") 

