#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 12 puzzle 2
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-03.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)


# In[ ]:


## PROBLEM DOMAIN code
from nbodysystem import *


# In[ ]:


#class statics:
#  str_2_sys_re = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')


# In[ ]:


def solve(inputs: str) -> int:
  nbs = get_sys_from_str(inputs)
  #nbs.iterate()
  nbs.iterate(tm_steps=2)
  return 0


# In[ ]:


## MAIN


# In[ ]:


### tests


# In[ ]:


## example 1
ins = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
""".strip()
log.debug(f"ins=\n{ins}")

nbs = get_sys_from_str(ins)
tm0_pos_id = nbs.get_id()
log.info(f"nbs {nbs} pos_id={tm0_pos_id}")
seen = {}
seen[tm0_pos_id] = True

found_tm = -1
for i in range(10000):
  nbs.iterate()
  k = nbs.get_id()
  if k in seen:
    log.warning(f"found repetition in {nbs}")
    found_tm = nbs.tm
    break
  else:
    seen[k] = True
res = found_tm

expectd = 2772
aoc.assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)


# In[ ]:


# example 2


# In[ ]:


### personal input solution


# In[ ]:


ins = aoc.read_file_to_str("day12.in")
log.info(f"input={ins}")
nbs = get_sys_from_str(ins)
res = 0
print(f"result={res}")

