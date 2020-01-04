#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 7 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-03.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


# In[ ]:


def cl(l: list) -> str:
  """Return compact list representation as str."""
  return f"[{','.join(map(str,l))}]"


# In[ ]:


## PROBLEM DOMAIN code
import itertools
from lib.intcode_interpreter import *


# In[ ]:


def chain_amps_feedback(program: list, combi: list, max_loops=1e9):
  amps = []
  for i in range(5):
    amp = IntcodeInterpreter(program)
    amp.store_int_stdin(combi[i])
    amps.append(amp)
  lastval = 0
  loop = 1
  result = []
  while(loop <= max_loops and amps[-1].state != IntcodeInterpreter.STATE_HALTED):
    log.debug(f"LOOP {loop}")
    res = [lastval]
    for i in range(5):
      amp = amps[i]
      amp.store_int_stdin(lastval)
      amp.interpret_program(pause_on_output = True)
      if amp.state == amp.STATE_PAUSED:
        assert 1 == len(amp.pseudo_stdout), f"only one output expected for amp {i}"
        lastval = amp.fetch_int_stdout()
        res.append(lastval)
        log.debug(f"  amp {i} OUT => {lastval}")
      elif amp.state == IntcodeInterpreter.STATE_HALTED:
        log.debug(f"  amp {i} HALTED")
    result.append(res)
    loop += 1
  #print(f"all results={result}")
  log.debug(f"chain_amps_feedback num-loops={loop}")
  return res[-1]


# In[ ]:


def solve(program: list, base_combi: list) -> list:
  combis = list(itertools.permutations(base_combi, len(base_combi)))
  log.info(f"len-combis={len(combis)}")

  idx = 0
  max_idx = -1
  max_val = -1
  for combi in combis:
    val = chain_amps_feedback(program, combi)
    if val > max_val:
      max_idx = idx
      max_val = val
    idx += 1
  log.info(f"optimal val={max_val} found for combi={combis[max_idx]} @iter={max_idx+1} of {len(combis)}")
  return [combis[max_idx], max_val]


# In[ ]:


## MAIN


# In[ ]:


### tests
log.setLevel(logging.DEBUG)


# In[ ]:


# example "1" of puzzle 1, recalculated
ins = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
combi = [4,3,2,1,0]

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps_feedback(ins, combi, max_loops=2)
print(f"result out={result}")
expected = 43210
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example "1"
log.setLevel(logging.INFO)
ins = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
  27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
combi = [9,8,7,6,5]

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps_feedback(ins, combi)
print(f"result out={result}")
expected = 139629729
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


result = solve(ins, [5,6,7,8,9])
print(f"result out={result}")


# In[ ]:


# example "2"
ins = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
combi = [9,7,8,5,6]

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps_feedback(ins, combi)
print(f"result out={result}")
expected = 18216
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


result = solve(ins, [5,6,7,8,9])
print(f"result out={result}")


# In[ ]:


### personal input solution
data = aoc.read_file_firstline_to_str('day07.in')
data = list(map(int, data.split(',')))
log.info(f"data-type={type(data)} data=\n{cl(data)}")

result = solve(data, [5,6,7,8,9])
print(f"result out={result}")

