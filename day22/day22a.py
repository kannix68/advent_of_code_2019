#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 22 puzzle 1
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
import re
#from timeit import default_timer as timer  # performance timing measurement


# In[ ]:


def parse_commands(cmd_strs: List[str]) -> list:
  cmds = []
  cut_re = re.compile(r'(cut) (-?\d+)')
  dealinc_re = re.compile(r'(deal with increment) (-?\d+)')
  for cmdstr in cmd_strs:
    if cmdstr == "deal into new stack":
      cmd = ['new_stack', None]
    elif cmdstr.startswith('cut '):
      m = cut_re.match(cmdstr)
      p1 = int(m.group(2))
      cmd = ['cut', p1]
    elif cmdstr.startswith('deal with increment '):
      m = dealinc_re.match(cmdstr)
      p1 = int(m.group(2))
      cmd = ['dealinc', p1]
    else:
      raise(RuntimeError(f"unparsed command {cmdstr}!"))
    cmds.append(cmd)
  #log.info(f"parse_commands: returns {cmds}")
  return cmds


# In[ ]:


def shuffle_cards_cmds(cards_num: int, cmds: list):
  cards = list(range(cards_num))
  cards_len = len(cards)
  for cmd in cmds:
    c, p = cmd[0], cmd[1]
    if c == 'new_stack':
      cards.reverse()
    elif c == 'cut':
      if p > 0:
        cards = cards[p:] + cards[0:p]
      elif p < 0:
        cards = cards[p:] + cards[0:cards_len+p]
      else:
        raise(RuntimeError(f"unhandled cut param {p}!"))
    elif c == 'dealinc':
      if p > 0:
        outcards = cards.copy()
        for idx, val in enumerate(cards):
          outcards[(idx*p) % cards_len] = val
        cards = outcards
      else:
        raise(RuntimeError(f"unhandled dealinc param {p}!"))
    else:
      raise(RuntimeError(f"unhandled command {cmd}!"))
  #log.info(f"shuffle_cards_cmds: returns {cards}")
  return cards


# In[ ]:


## MAIN


# In[ ]:


### tests


# In[ ]:


## example 1
cards_num = 10
cmds_str = ["deal into new stack"]
expected = '9 8 7 6 5 4 3 2 1 0'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 2
cards_num = 10
cmds_str = ["cut 3"]
expected = '3 4 5 6 7 8 9 0 1 2'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 3
cards_num = 10
cmds_str = ["cut -4"]
expected = '6 7 8 9 0 1 2 3 4 5'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 4
cards_num = 10
cmds_str = ["deal with increment 3"]
expected = '0 7 4 1 8 5 2 9 6 3'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example multi-1
ins = """
deal with increment 7
deal into new stack
deal into new stack
""".strip()
cards_num = 10
cmds_str = ins.split("\n")
expected = '0 3 6 9 2 5 8 1 4 7'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example multi-2
ins = """
cut 6
deal with increment 7
deal into new stack
""".strip()
cards_num = 10
cmds_str = ins.split("\n")
expected = '3 0 7 4 1 8 5 2 9 6'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example multi-3
ins = """
deal with increment 7
deal with increment 9
cut -2
""".strip()
cards_num = 10
cmds_str = ins.split("\n")
expected = '6 3 0 7 4 1 8 5 2 9'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example multi-4
ins = """
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
""".strip()
cards_num = 10
cmds_str = ins.split("\n")
expected = '9 2 5 8 1 4 7 0 3 6'

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = ' '.join(map_e(str, cards))
aoc.assert_msg(f"input={cards_num}, #cmds={len(cmds)} expects output={expected}, got {result}", expected == result)

#log.info(type(cards[0]))
log.info(cards.index(2))


# In[ ]:


### personal input solution


# In[ ]:


log.setLevel(logging.INFO)
data = aoc.read_file_to_str("day22.in").strip()
log.info(f"data-len={len(data)}, data={data[:40]}...")

cards_num = 10007
cmds_str = data.split("\n")

cmds = parse_commands(cmds_str)
cards = shuffle_cards_cmds(cards_num, cmds)
result = cards.index(2019)
print(f"result pos={result}")  # 0-based "position" index

