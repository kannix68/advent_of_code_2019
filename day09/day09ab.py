#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 9 puzzle 1 and pzzle 2
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
import itertools
from lib.intcode_interpreter import *


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
ins = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

computer = IntcodeInterpreter(ins, mem_growable=True)
print(f"mem-type={type(computer.mem)}, mem-len={len(computer.mem)}")
computer.interpret_program()
result = computer.pseudo_stdout
print(f"post mem-len={len(computer.mem)}")
print(f"result={result}")

expected = ins
aoc.assert_msg(f"input={aoc.cl(ins)} expects output={aoc.cl(expected)}, got {aoc.cl(result)}", expected == result)


# In[ ]:


# example "2"
ins = [1102,34915192,34915192,7,4,7,99,0]

computer = IntcodeInterpreter(ins, mem_growable=True)
print(f"mem-type={type(computer.mem)}, mem-len={len(computer.mem)}")
computer.interpret_program()
result = computer.pseudo_stdout
print(f"post mem-len={len(computer.mem)}")
print(f"result={result}")

expected = 16
aoc.assert_msg(f"input={aoc.cl(ins)} expects output digits={expected}, got {aoc.cl(result)}", expected == len(str(result[-1])))


# In[ ]:


# example "3"
ins = [104,1125899906842624,99]

computer = IntcodeInterpreter(ins, mem_growable=True)
print(f"mem-type={type(computer.mem)}, mem-len={len(computer.mem)}")
computer.interpret_program()
result = computer.pseudo_stdout[-1]
print(f"post mem-len={len(computer.mem)}")
print(f"result={result}")

expected = 1125899906842624
aoc.assert_msg(f"input={aoc.cl(ins)} expects output={expected}, got {result}", expected == result)


# In[ ]:


### personal input solution, puzzle 1
data = aoc.read_file_firstline_to_str('day09.in')
data = list(map(int, data.split(',')))
log.info(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = IntcodeInterpreter(data, mem_growable=True)
print(f"mem-type={type(computer.mem)}, mem-len={len(computer.mem)}")
computer.store_int_stdin(1)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"post mem-len={len(computer.mem)}")
print(f"result={result}")


# In[ ]:


### personal input solution, puzzle 2
#data = aoc.read_file_firstline_to_str('day09.in')
#data = list(map(int, data.split(',')))
#log.info(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = IntcodeInterpreter(data, mem_growable=True)
print(f"mem-type={type(computer.mem)}, mem-len={len(computer.mem)}")
computer.store_int_stdin(2)
computer.interpret_program()
result = computer.pseudo_stdout
print(f"post mem-len={len(computer.mem)}, incruction-count={computer.ctr}")
print(f"result={result}")

