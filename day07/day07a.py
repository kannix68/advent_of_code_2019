#!/usr/bin/env python
# coding: utf-8

# In[1]:


##
# Advent of code 2019, AoC day 7 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-03.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[2]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)


# In[3]:


def cl(l: list) -> str:
  """Return compact list representation as str."""
  return f"[{','.join(map(str,l))}]"


# In[4]:


## PROBLEM DOMAIN code
import itertools
from lib.intcode_interpreter import *


# In[5]:


def chain_amps(program: list, combi: list):
  amps = []
  for i in range(5):
    amp = IntcodeInterpreter(program)
    amp.store_int_stdin(combi[i])
    amps.append(amp)
  lastval = 0
  res = [lastval]
  for i in range(5):
    amp = amps[i]
    amp.store_int_stdin(lastval)
    amp.interpret_program()
    lastval = amp.pseudo_stdout[-1]
    res.append(lastval)
  return res[-1]


# In[6]:


## MAIN


# In[7]:


### tests


# In[8]:


# example "0"
ins = []
combi = [3,1,2,4,0]

# example "1"
ins = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
combi = [4,3,2,1,0]

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps(ins, combi)
print(f"result out={result}")
expected = 43210
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[9]:


# example "2"
ins = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
  101,5,23,23,1,24,23,23,4,23,99,0,0]
combi = [0,1,2,3,4]
expected = 54321

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps(ins, combi)
print(f"result out={result}")
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[10]:


# example "2"
ins = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
  1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
combi = [1,0,4,3,2]
expected = 65210

param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
result = chain_amps(ins, combi)
print(f"result out={result}")
aoc.assert_msg(f"input={cl(ins)} with param={param} expects output={expected}, got {result}", expected == result)


# In[11]:


### personal input solution
data = aoc.read_file_firstline_to_str('day07.in')
data = list(map(int, data.split(',')))
print(f"data-type={type(data)} data=\n{cl(data)}")

# just check first combination manually:
base_combi = [0,1,2,3,4]
result = chain_amps(data, combi)
print(f"result={result}")

combis = list(itertools.permutations(base_combi, len(base_combi)))
print(f"len-combis={len(combis)}")

idx = 0
max_idx = -1
max_val = -1
for combi in combis:
  val = chain_amps(data, combi)
  if val > max_val:
    max_idx = idx
    max_val = val
  idx += 1
print(f"optimal val={max_val} found for combi={combis[max_idx]} @iter={max_idx} of {len(combis)}")

