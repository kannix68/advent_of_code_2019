#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 13 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-04.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


# In[ ]:


## PROBLEM DOMAIN code
from collections import defaultdict
from collections import OrderedDict
#import itertools
from lib.intcode_interpreter import *


# In[ ]:


def make_grid(inlist: list) -> dict:
  outlist = rearrange_list(inlist, 3)
  #log.debug(outlist)    
  grid = {}
  for o in outlist:
    c = tuple([o[0], o[1]])
    t = o[2]
    if c in grid:
      # already seen
      raise(RuntimeError(f"object-check not implemented, {o}"))
    grid[c] = t
  return grid


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
outputs = [1,2,3,6,5,4]
grid = make_grid(outputs)
log.debug(grid)


# In[ ]:


### personal input solution, puzzle 1
log.setLevel(logging.INFO)
data = aoc.read_file_firstline_to_str('day13.in')
data = list(map(int, data.split(',')))
log.debug(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = IntcodeInterpreter(data, mem_growable=True)
computer.interpret_program()
outputs = computer.pseudo_stdout
#log.debug(outputs[:100])
grid = make_grid(outputs)
#log.info(f"grid={list(grid[:100])} ...")
print(f"found {len(grid.keys())} objects")
obj_counts = defaultdict(int)
for c in grid.keys():
  v = grid[c]
  obj_counts[v] += 1
print(f"result={OrderedDict(sorted(obj_counts.items()))}")


# In[ ]:




