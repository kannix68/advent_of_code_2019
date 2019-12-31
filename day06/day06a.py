#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 6 puzzle 1
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
  dist_sum = 0
  for node in g.nodes():
    if node != "COM":
      dist = len(nx.shortest_path(g, source=node, target="COM")) - 1
      dist_sum += dist
      print(f"{node}: dist={dist}")
    else:
      print(f"{node}!")
  return dist_sum


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
""".strip().split("\n")
print(f"ins={ins}")
expectd = 42
res = solve(ins)
aoc.assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)


# In[ ]:


### personal input solution


# In[ ]:


ins = aoc.read_file_to_list("day06.in")
#print(f"{ins}")
res = solve(ins)
print(f"sum of orbits={res}")
