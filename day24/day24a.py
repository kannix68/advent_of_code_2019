#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 24 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-07.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
from typing import Dict, List, Tuple
import lib.aochelper as aoc
from lib.aochelper import map_e


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


# In[ ]:


## PROBLEM DOMAIN code
import hashlib
#import re
#from timeit import default_timer as timer  # performance timing measurement


# In[ ]:


def iterate_world(world: List[str], num_iters=1, break_on_duplicate=False) -> List[str]:
  if break_on_duplicate:
    world_hashes = []
    world_md5 = hashlib.md5("\n".join(world).encode()).hexdigest()
    world_hashes.append(world_md5)
    #log.debug(f"new hash={world_md5}")
  for iter in range(int(num_iters)):
    if iter > 0:
      world = out_world.copy()
    out_world = []
    for y, line in enumerate(world):
      #log.debug(f"line={line}")
      out_line = []
      for x, val in enumerate(line):
        #log.debug(f"cell={val}")
        nb = ''.join(aoc.get_neighbors(world, x, y)).count('#')
        if val == '#':
          if nb == 1:
            out_line.append('#')
          else:
            out_line.append('.')
        else:
          if nb == 1 or nb == 2:
            out_line.append('#')
          else:
            out_line.append('.')
      out_world.append(''.join(out_line))
    wrep = "\n".join(out_world)
    #log.debug(f"iter#{iter+1} out-world=\n{wrep}")
    if break_on_duplicate:
      world_md5 = hashlib.md5("\n".join(out_world).encode()).hexdigest()
      if world_md5 in world_hashes:
        log.info(f"iter#{iter+1} duplicate world on #={iter+1} found from previous #={world_hashes.index(world_md5)+1}=; world=\n{wrep}")
        break
      else:
        world_hashes.append(world_md5)
        #log.debug(f"new hash={world_md5}")
  log.info(f"finish iter#{iter+1} out-world=\n{wrep}")
  return out_world


# In[ ]:


def calc_biodiv(world: List[str]) -> int:
  biodiv = 0
  linesize = len(world[0])
  for y, line in enumerate(world, 0):
    for x, val in enumerate(line, 1):
      if val == '#':
        log.debug(f"found bio @ ({x}, {y}) idx={y*linesize+x}, val={2**(y*linesize+x-1)}")
        biodiv += 2**(y*linesize+x-1)
  return biodiv


# In[ ]:


## MAIN


# In[ ]:


### tests
log.setLevel(logging.DEBUG)


# In[ ]:


## example 1
ins = """
....#
#..#.
#..##
..#..
#....
""".strip()

inworld = ins.split("\n")
outworld = iterate_world(inworld, num_iters=100, break_on_duplicate=True)
outrep = "\n".join(outworld)
log.info(f"result=\n{outrep}")
biodiv = calc_biodiv(outworld)
log.info(f"biodiv={biodiv}")

#result = ' '.join(map_e(str, cards))
#aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


### personal input solution


# In[ ]:


log.setLevel(logging.INFO)
data = aoc.read_file_to_str("day24.in").strip()
log.info(f"data-len={len(data)}, data={data[:40]}...")

inworld = data.split("\n")
outworld = iterate_world(inworld, num_iters=100, break_on_duplicate=True)
outrep = "\n".join(outworld)
log.info(f"result=\n{outrep}")
biodiv = calc_biodiv(outworld)
log.info(f"biodiv={biodiv}")

