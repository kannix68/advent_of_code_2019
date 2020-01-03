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


# example "1", zero input
ins = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9] # "using position mode"
param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 0
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example "1", non-zero input
ins = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9] # "using position mode"
param = 99 # "output 0 if the input was zero or 1 if the input was non-zero"
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 1
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example "2", zero input
ins = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1] # "using immediate mode"
param = 0 # "output 0 if the input was zero or 1 if the input was non-zero"
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 0
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# example "2", non-zero input
ins = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1] # "using immediate mode"
param = 999 # "output 0 if the input was zero or 1 if the input was non-zero"
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 1
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# "larger" example "3", input < 8
ins = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# output 999 if the input value is below 8,
# output 1000 if the input value is equal to 8,
# or output 1001 if the input value is greater than 8.
param = 7 #
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 999
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# "larger" example "3", input == 8
ins = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# output 999 if the input value is below 8,
# output 1000 if the input value is equal to 8,
# or output 1001 if the input value is greater than 8.
param = 8 #
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 1000
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:


# "larger" example "3", input > 8
ins = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
  1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
  999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# output 999 if the input value is below 8,
# output 1000 if the input value is equal to 8,
# or output 1001 if the input value is greater than 8.
param = 9 #
computer = IntcodeInterpreter(ins)
computer.store_int_stdin(param)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"result out={result}")
result = result[0]
expected = 1001
aoc.assert_msg(f"input={ins} with param={param} expects output={expected}, got {result}", expected == result)


# In[ ]:





# In[ ]:


### personal input solution
data = aoc.read_file_firstline_to_str('day05.in')
data = list(map(int, data.split(',')))
print(f"data-type={type(data)} data={data}")

computer = IntcodeInterpreter(data)
computer.store_int_stdin(5)
computer.interpret_program()
#result = computer.mem
result = computer.pseudo_stdout
print(f"result={result}")

