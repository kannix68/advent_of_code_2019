#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 6 puzzle 2
# This solution (python3.7 jupyter notebook) by kannix68, @ 2019-12-30.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


## PROBLEM DOMAIN code
import networkx as nx  # Graph theory module


# In[ ]:


def solve(inputs):
  g = nx.Graph()
  for relat in inputs:
    orbit = relat.split(")")
    g.add_node(orbit[0])
    g.add_node(orbit[1])
    g.add_edge(orbit[0], orbit[1])
  dist = len(nx.shortest_path(g, source="YOU", target="SAN")) - 3
  # -3 because: Direct orbit of YOU and SAN not counted,
  #   and transfers (not number) between planets requested.
  return dist


# In[ ]:


## MAIN


# In[ ]:


### tests


# In[ ]:


ins = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".strip().split("\n")
print(f"ins={ins}")
expectd = 4
res = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)


# In[ ]:


### personal input solution


# In[ ]:


ins = aoc.read_file_to_list("day06.in")
#print(f"{ins}")
res = solve(ins)
print(f"result={res}")
