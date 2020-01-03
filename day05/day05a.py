#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 5 puzzle 1
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
from intcode_interpreter import *


# In[ ]:


## MAIN


# In[ ]:


### tests


# In[ ]:


# example "1"
ins = [3,0,4,0,99] # "The program 3,0,4,0,99 outputs whatever it gets as input, then halts."
param = 7
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
#result = computer.mem
result = computer.pseudo_stdout[0]
expected = param
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example "1", another input
ins = [3,0,4,0,99] # "The program 3,0,4,0,99 outputs whatever it gets as input, then halts."
param = 88
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
#result = computer.mem
result = computer.pseudo_stdout[0]
expected = param
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


### personal input solution
data = aoc.read_file_firstline_to_str('day05.in')
data = list(map(int, data.split(',')))
print(f"data-type={type(data)} data={data}")

computer = IntcodeInterpreter(data)
computer.store_int_stdin(1)
computer.interpret_program()
#result = computer.mem
result = computer.pseudo_stdout
print(f"result={result}")

