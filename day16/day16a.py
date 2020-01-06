#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 16 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-06.

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
import itertools


# In[ ]:


def phase_transform(ins: str, ptrn: List[int], num_phases = 1) -> str:
  tmp = ins
  for iter in range(num_phases):
    if iter > 0:
      tmp = outs
    outdigs = []
    for digidx in range(len(ins)):
      digptrn = []
      for i in ptrn:
        for fac in range(digidx+1):
          digptrn.append(i)
      #log.debug(f"digid={digidx}, digptrn={digptrn}")
      outdig_compositor = []
      offset = 1  # number of elements to consume from (cycled) pattern before acting on input
      for idx, val in enumerate(itertools.cycle(digptrn), -offset):
        if idx == len(tmp):
          break
        if idx < 0:
           continue
        #log.debug(f"  {idx}, ins-dig={ins[idx]} ptrn:{val}")
        outdig_compositor.append( int(tmp[idx])*val )
      dig = abs(sum(outdig_compositor))%10
      outdigs.append(dig)
      outs = ''.join(map_e(str, outdigs))
    log.debug(f"phase_transform #{iter+1}: outdigs={outs} via {len(ins)} iters from ptrn={aoc.cl(ptrn)}, input#={tmp}")

  log.info(f"phase_transform iter={iter+1} out={outs} via {len(ins)} iters from ptrn={aoc.cl(ptrn)}, input0={ins}")
  return outs


# In[ ]:


## MAIN


# In[ ]:


### tests
log.setLevel(logging.INFO)


# In[ ]:


## example 0-a from text
ins = "9, 8, 7, 6, 5"
ins = map_e(int, ins.split(', '))
ptrn = "1, 2, 3"
ptrn = map_e(int, ptrn.split(', '))
res = phase_transform(ins, ptrn)
log.info(f"result={res}")

#result = solve(ins)
#expected = 31
#aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 1
ins = "12345678"
ptrn = [0, 1, 0, -1]
res = phase_transform(ins, ptrn)
log.info(f"result iter#1={res}")
res = phase_transform(res, ptrn)
log.info(f"result iter#1={res}")

result = phase_transform(ins, ptrn, num_phases=4)
expected = "01029498"
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example 2
ins = "80871224585914546619083218645595"
ptrn = [0, 1, 0, -1]
result = phase_transform(ins, ptrn, num_phases=100)
result = result[:8]
expected = "24176176"
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example 3
ins = "19617804207202209144916044189917"
ptrn = [0, 1, 0, -1]
result = phase_transform(ins, ptrn, num_phases=100)
result = result[:8]
expected = "73745418"
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example 4
ins = "69317163492948606335995924319873"
ptrn = [0, 1, 0, -1]
result = phase_transform(ins, ptrn, num_phases=100)
result = result[:8]
expected = "52432133"
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


### personal input solution


# In[ ]:


log.setLevel(logging.INFO)
data = aoc.read_file_to_str("day16.in").strip()
ptrn = [0, 1, 0, -1]
log.info(f"data=\n{data}")
#res = solve(data)
result = phase_transform(data, ptrn, num_phases=100)
result = result[:8]
print(f"result={result}")

