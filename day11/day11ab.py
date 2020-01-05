#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 11 puzzle 1 and puzzle 2
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


# 0 is turn left, 1 is turn right
rotations = { 0: {"up":"left", "left":"down", "down":"right", "right":"up"},
 1: {"up":"right", "right":"down", "down":"left", "left":"up"} }


# In[ ]:


def get_coord_color():
  log.debug(f"get_coord_color current-corrd={cur_coord} val={seen_coords[cur_coord]}")
  return seen_coords[cur_coord]


# In[ ]:


def paint_coord_color(i):
  global seen_coords
  global painted_coords
  seen_coords[cur_coord] = i
  painted_coords[cur_coord] = i


# In[ ]:


def turn_dir_and_move1(i):
  global cur_dir
  global cur_coord
  new_dir = rotations[i][cur_dir]
  cur_dir = new_dir
  log.debug(f"turn_dir_and_move1 new dir={cur_dir}")
  if cur_dir == "up":
    cur_coord = tuple([cur_coord[0],cur_coord[1]+1])
  elif cur_dir == "down":
    cur_coord = tuple([cur_coord[0],cur_coord[1]-1])
  elif cur_dir == "right":
    cur_coord = tuple([cur_coord[0]+1,cur_coord[1]])
  elif cur_dir == "left":
    cur_coord = tuple([cur_coord[0]-1,cur_coord[1]])
  log.debug(f"  turn_dir_and_move1 new coord={cur_coord}")
  if not cur_coord in seen_coords:
    log.debug(f"    turn_dir_and_move1 new first-visited coord={cur_coord}")
    seen_coords[cur_coord] = 0


# In[ ]:


def init_simulator():
  global seen_coords
  global painted_coords
  global cur_coord
  global cur_dir
  seen_coords = {}
  painted_coords = {}
  cur_coord = tuple([0,0])
  cur_dir = "up"
  seen_coords[cur_coord] = 0
  computer = IntcodeSimulator([], mem_growable=False)
  return computer


# In[ ]:


def init_interpreter(program):
  global seen_coords
  global painted_coords
  global cur_coord
  global cur_dir
  seen_coords = {}
  painted_coords = {}
  cur_coord = tuple([0,0])
  cur_dir = "up"
  seen_coords[cur_coord] = 0   # initial state "unpainted black"
  computer = IntcodeInterpreter(program, mem_growable=True)
  return computer


# In[ ]:


def simulate_cell_commands(computer, l):
  computer.next_pause_for_input()
  computer.interpret_program(pause_on_output=True, pause_on_input=True)
  computer.store_int_stdin(get_coord_color())
  computer.next_consume_input()

  computer.next_output(l[0])
  computer.interpret_program(pause_on_output=True, pause_on_input=True)
  paint_coord_color(computer.fetch_int_stdout())

  computer.next_output(l[1])
  computer.interpret_program(pause_on_output=True, pause_on_input=True)
  turn_dir_and_move1(computer.fetch_int_stdout())
  log.info(f"seen-coords={seen_coords}")


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
computer = init_simulator()
computer.next_pause_for_input()
computer.interpret_program(pause_on_output=True, pause_on_input=True)
assert computer.waits_for_input(), "should wait for intput"
computer.store_int_stdin(get_coord_color())
log.debug(f"computer.pseudo_stdin={computer.pseudo_stdin}")

computer.next_consume_input()
computer.next_output(1)
computer.interpret_program(pause_on_output=True, pause_on_input=True)
assert computer.has_output(), "should have output"
v = computer.fetch_int_stdout()
assert 1 == v, "output should be 1"
paint_coord_color(v)

computer.next_output(0)
computer.interpret_program(pause_on_output=True, pause_on_input=True)
assert computer.has_output(), "should have_output"
v = computer.fetch_int_stdout()
assert 0 == v, "output should be 0"
turn_dir_and_move1(v)
log.info(seen_coords)


computer.next_pause_for_input()
computer.interpret_program(pause_on_output=True, pause_on_input=True)
computer.store_int_stdin(get_coord_color())

computer.next_consume_input()
computer.next_output(0)
computer.interpret_program(pause_on_output=True, pause_on_input=True)
paint_coord_color(computer.fetch_int_stdout())

computer.next_output(0)
computer.interpret_program(pause_on_output=True, pause_on_input=True)
turn_dir_and_move1(computer.fetch_int_stdout())
log.info(seen_coords)


simulate_cell_commands(computer, [1,0])
simulate_cell_commands(computer, [1,0])

simulate_cell_commands(computer, [0,1])
simulate_cell_commands(computer, [1,0])
simulate_cell_commands(computer, [1,0])

log.info(f"seen={len(seen_coords.keys())} painted={len(painted_coords.keys())}")


# In[ ]:


### personal input solution, puzzle 1
log.setLevel(logging.INFO)
data = aoc.read_file_firstline_to_str('day11.in')
data = list(map(int, data.split(',')))
log.info(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = init_interpreter(data)
max_iter = 1e7
i = 0
sub_cmd = 0
while (computer.state != IntcodeInterpreter.STATE_HALTED) and i < max_iter:
  i += 1
  computer.interpret_program(pause_on_output=True, pause_on_input=True)
  if computer.waits_for_input():
    computer.store_int_stdin(get_coord_color())
  elif computer.has_output():
    if sub_cmd == 0:
      paint_coord_color(computer.fetch_int_stdout())
      sub_cmd = 1
    elif sub_cmd == 1:
      turn_dir_and_move1(computer.fetch_int_stdout())
      sub_cmd = 0

result = painted_coords
print(f"res-len={len(result)} state={computer.state}, i={i+1}")


# In[ ]:


### personal input solution, puzzle 2
#log.setLevel(logging.INFO)
#data = aoc.read_file_firstline_to_str('day11.in')
#data = list(map(int, data.split(',')))
#log.info(f"data-type={type(data)} data=\n{aoc.cl(data)}")

computer = init_interpreter(data)
seen_coords[cur_coord] = 1  # initial state "painted white"

max_iter = 1e7
i = 0
sub_cmd = 0
while (computer.state != IntcodeInterpreter.STATE_HALTED) and i < max_iter:
  i += 1
  computer.interpret_program(pause_on_output=True, pause_on_input=True)
  if computer.waits_for_input():
    computer.store_int_stdin(get_coord_color())
  elif computer.has_output():
    if sub_cmd == 0:
      paint_coord_color(computer.fetch_int_stdout())
      sub_cmd = 1
    elif sub_cmd == 1:
      turn_dir_and_move1(computer.fetch_int_stdout())
      sub_cmd = 0

result = painted_coords
print(f"res-len={len(result)} state={computer.state}, i={i+1}")

xmin = 9999
xmax = -9999
ymin = 9999
ymax = -9999

for coord in seen_coords.keys():
  if coord[0] < xmin:
    xmin = coord[0]
  if coord[0] > xmax:
    xmax = coord[0]
  if coord[1] < ymin:
    ymin = coord[1]
  if coord[1] > ymax:
    ymax = coord[1]
offset = [-xmin, -ymin]
print(f"dimensions = {[[xmin, xmax], [ymin, ymax]]}, offset={offset}")

ofs_x = offset[0]
ofs_y = offset[1]
rows2d = []
for row in range(ymax + ofs_y + 1):
  cur_row = []
  for col in range(xmax + ofs_x + 1):
    c = tuple([col-ofs_x, row-ofs_y])
    if c in seen_coords:
      if seen_coords[c] == 1:
        cur_row.append('#')
      else:
        cur_row.append(' ')
    else:
      cur_row.append('_')
  rows2d.append(cur_row)
rows2d.reverse()
print(aoc.represent_2d_char_list(rows2d))


# In[ ]:




