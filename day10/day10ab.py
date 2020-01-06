#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 10 puzzle 1 and 2
# This solution (python3.7 jupyter notebook) by kannix68, @ 2020-01-05.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


# In[ ]:


## PROBLEM DOMAIN code


# In[ ]:


# for arrays / 2d matrices,
import itertools
import math


# In[ ]:


def angle_eq(direction1, direction2):
  """Determine if two direction vectors (x,y) have the same angle."""
  dir1_0, dir1_1, dir2_0, dir2_1 = direction1[0], direction1[1], direction2[0], direction2[1]
  #-if aoc.sign(seen_d2[0])==aoc.sign(d2[0]) and aoc.sign(seen_d2[1])==aoc.sign(d2[1]) \
  #-  and d2[0] % seen_d2[0] == 0 and d2[1] % seen_d2[1] == 0:
  #math.atan2(dir2_1-dir1_1, dir2_0-dir1_0)
  at1 = math.atan2(dir1_1, dir1_0)
  at2 = math.atan2(dir2_1, dir2_0)
  delta = at1 - at2
  cond = abs(delta) < 1e-9
  #log.debug(f"angle_eq: dir1={direction1}, dir2={direction2}, atan2:1={at1}, atan2:2={at2}, cond={cond}")
  return cond


# In[ ]:


def get_space2d_from_str(s: str) -> list:
  space_2d = []
  for l in s.split("\n"):
    space_2d.append(list(l))
  log.debug(f"space=\n{aoc.represent_2d_char_list(space_2d)}")
  return space_2d


# In[ ]:


def get_bodies_list(space_2d: list) -> list:
  bodies = []
  for y in range(len(space_2d)):
    for x in range(len(space_2d[0])):
      if space_2d[y][x] == '#':
        c = tuple([x,y])
        log.debug(f"body found at {c}")
        bodies.append(c)
  log.info(f"found {len(bodies)} bodies")
  return bodies


# In[ ]:


def get_distances_from_bodies(bodies):
  """Returns a dict of dicts containing distances"""
  distances = {}
  combis = list(itertools.combinations(bodies, 2))
  log.info(f"to handle {len(combis)} body-combinations")
  for combi in combis:
    b1, b2 = combi
    log.debug(f"b1={b1}, b2={b2}")
    if not b1 in distances:
      distances[b1] = {}
    if not b2 in distances:
      distances[b2] = {}
    b1dists = distances[b1]
    b2dists = distances[b2]
    dist1 = abs(b2[0]-b1[0]) + abs(b2[1]-b1[1])
    dist2 = [b2[0]-b1[0], b2[1]-b1[1]]
    b1dists[b2] = {'dist1': dist1, 'dist2': dist2}  
    b2dists[b1] = {'dist1': dist1, 'dist2': list(map(lambda v: -v, dist2))}
    #log.debug(f"added distances {b1}=>{b1dists} and {b2}=>{b2dists}")
  return distances


# In[ ]:


def body_sees_bodies(b1: tuple, distances: dict) -> int:
  """Return how many bodies a given obersver-body can see in grid given by distances-dict-dict."""
  cur_dist = -1
  bodists = distances[b1]
  seen_dists = []
  seen_bodies = []
  for b2, b12dists in sorted(bodists.items(), key=lambda it: it[1]['dist1']): # it[0]=key, it[1]=value
    log.debug(f"b1={b1}->b2={b2} => {bodists[b2]}")
    d1, d2 = b12dists['dist1'], b12dists['dist2']
    if d1 > cur_dist:
      log.debug(f"new distance layer {d1}")
      cur_dist = d1
      seen_dists.append(cur_dist)
    if d1 < 2:
      seen_bodies.append([b2, d1, d2])
    else:
      blocked = False
      for sd in seen_dists:
        #if sd < d1 and d1 % sd == 0:  # current dist is multiple of a seen dist
        if sd >= d1:
          continue
        for bodylst in seen_bodies:  # search previously seen bodies
          if bodylst[1] == sd:  # only search current seen-distance
            seen_d2 = bodylst[2]
            # check for equal signs of x and y component of dist2d,
            #  then check for amounts exactly multiple of seen amounts:
            if angle_eq(d2, seen_d2):
              # for example1: from (1,0) [(4, 3), 6, [3, 3]] SHOULD BE blocked by (3, 2), 4, [2, 2]
              log.debug(f"b1={b1}->b2={b2} d1={d1},d2={d2} IS BLOCKED by {bodylst}")
              blocked = True      
      if not blocked:
        seen_bodies.append([b2, d1, d2])
  log.debug(f"seen # {len(seen_bodies)} bodies={seen_bodies}")
  return len(seen_bodies)


# In[ ]:


def get_body_max_seeing(distances: dict) -> list:
  body_num = 0
  max_seen_body = tuple([-1,-1])
  max_seen_num = 0
  for b1 in distances.keys():
    body_num += 1
    #if body_num > 1:
    #  log.warning("fail loop for DEBUG")
    #  break
    log.debug(f"current #{body_num} b1={b1}!")
    seen_bodies_num = body_sees_bodies(b1, distances)
    if seen_bodies_num > max_seen_num:
      max_seen_num = seen_bodies_num
      max_seen_body = b1
      log.debug(f"new max-seen body={max_seen_body} sees {max_seen_num} bodies")
  return [max_seen_body, max_seen_num]


# In[ ]:


def solve(ins: str) -> int:
  """Return max seen bodies."""
  space_2d = get_space2d_from_str(ins)
  bodies = get_bodies_list(space_2d)
  distances = get_distances_from_bodies(bodies)
  reslst = get_body_max_seeing(distances)
  log.info(f"reslst(body,seen-bodies)={reslst}")
  return reslst[1]


# In[ ]:


## MAIN


# In[ ]:


### tests
log.setLevel(logging.INFO)


# In[ ]:


## example 1
ins = """
.#..#
.....
#####
....#
...##
""".strip()
#log.debug(f"ins=\n{ins}")

result = solve(ins)
expected = 8
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 3
ins = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""".strip()
result = solve(ins)
expected = 33
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 4
ins = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
""".strip()
result = solve(ins)
expected = 35
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 5
ins = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
""".strip()
result = solve(ins)
expected = 41
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


## example 6
ins = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()
ex6_ins = ins # store for later use
result = solve(ins)
expected = 210
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)


# In[ ]:


### personal input solution


# In[ ]:


log.setLevel(logging.INFO)
data = aoc.read_file_to_str("day10.in").strip()
log.info(f"data=\n{data}")
res = solve(data)
print(f"result={res}")


# In[ ]:


## PUZZLE 2


# In[ ]:


def dist_between(a, b):
  """Return 2d distance between 2 2d points, seen from point a."""
  return [b[0]-a[0], b[1]-a[1]]


# In[ ]:


## Continuous 0..2*PI starting from direction north.
def angle_to(x: int, y: int) -> int:
  """Return angle for given vector pointing from orign (0,0), adjusted for north=0"""
  #xt,yt = y,x
  #rad = math.atan2(yt,xt)
  rad = math.atan2(x,y)
  if rad < 0.0:
    rad = math.pi + (math.pi + rad)
  return rad


# In[ ]:


def distsq_to(x: int, y: int) -> int:
  return x*x + y*y


# In[ ]:


a = angle_to(0,1)
assert aoc.fcmp(a,0), f"north expected=0, found={a}"

a = angle_to(1,0)
e = math.pi/2
t = aoc.fcmp(a,e)
assert t, f"east expected={e}, found={a} validating {t}"

a = angle_to(0,-1)
e = math.pi
assert aoc.fcmp(a,e), f"south expected={e}, found={a} validating {t}"

a = angle_to(-1,-1)
e = math.pi + math.pi/4
assert aoc.fcmp(a,e), f"south-west expected={e}, found={a} validating {t}"

a = angle_to(-1,0)
e = 1.5 * math.pi
assert aoc.fcmp(a,e), f"south-west expected={e}, found={a} validating {t}"


# In[ ]:


dist_between([-1,-1], [1,2])


# In[ ]:


def solve2(ins: str) -> int:
  """Return max seen bodies."""
  space_2d = get_space2d_from_str(ins)
  bodies = get_bodies_list(space_2d)
  distances = get_distances_from_bodies(bodies)
  reslst = get_body_max_seeing(distances)
  log.info(f"reslst(body,seen-bodies)={reslst}")
  return reslst


# In[ ]:


def rotate_laser(base, seen_bodies):
  destroyed_bodies = []
  bodies_ang_dist = {}
  for body in seen_bodies:
    vec = dist_between(base, body)
    dsq = distsq_to(vec[0], vec[1])
    ang = angle_to(vec[0], -vec[1])
    log.debug(f"bs={base}->b2={body}: vec={vec}, dsq={dsq}, angle={ang}")
    if not ang in bodies_ang_dist:
      bodies_ang_dist[ang] = {}
    bodies_ang_dist[ang][dsq] = body
  log.debug(f"bodies_ang_dist={bodies_ang_dist}")

  rot_num = 0
  while(len(bodies_ang_dist.keys()) > 0):
    rot_num +=1
    for ang in sorted(bodies_ang_dist.keys()):
      for dist in sorted(bodies_ang_dist[ang].keys()):
        log.debug(f"DESTROY ang={ang}, dist={dist}, body={bodies_ang_dist[ang][dist]}")
        destroyed_bodies.append(bodies_ang_dist[ang][dist])
        del bodies_ang_dist[ang][dist]
        break
      if len(bodies_ang_dist[ang].keys()) <= 0:
        log.debug(f"remove angle {ang}")
        del bodies_ang_dist[ang]
        #continue
  log.info(f"rotate_laser: finished in rotation {rot_num}, destroyed {len(destroyed_bodies)} bodies")
  return destroyed_bodies


# In[ ]:


## example 2-1
ins = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
""".strip().replace('X','#')

space_2d = get_space2d_from_str(ins)
bodies = get_bodies_list(space_2d)
distances = get_distances_from_bodies(bodies)
body_max_seeing = get_body_max_seeing(distances)

result = body_max_seeing[0]
expected = tuple([8, 3])
aoc.assert_msg(f"input={ins} expects output={expected}, got {result}", expected == result)

base = result
log.info(f"base is {base}")
seen_bodies = distances[base].keys()
l = rotate_laser(base, seen_bodies)


# In[ ]:


## example 2-2
ins = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()
space_2d = get_space2d_from_str(ins)
bodies = get_bodies_list(space_2d)
distances = get_distances_from_bodies(bodies)
body_max_seeing = get_body_max_seeing(distances)
base = body_max_seeing[0]
log.info(f"base is {base}")
seen_bodies = distances[base].keys()
l = rotate_laser(base, seen_bodies)
log.info(f"destroyed {l}")
trg = l[199]
trg2 = trg[0]*100+trg[1]
log.info(f"destroyed 200th={trg} => {trg2}")


# In[ ]:


## personal input solution, puzzle 2
log.setLevel(logging.INFO)
data = aoc.read_file_to_str("day10.in").strip()
log.info(f"data=\n{data}")

space_2d = get_space2d_from_str(data)
bodies = get_bodies_list(space_2d)
distances = get_distances_from_bodies(bodies)
body_max_seeing = get_body_max_seeing(distances)
base = body_max_seeing[0]
log.info(f"base is {base}")
seen_bodies = distances[base].keys()
l = rotate_laser(base, seen_bodies)
log.info(f"destroyed {l}")
trg = l[199]
trg2 = trg[0]*100+trg[1]
log.info(f"destroyed 200th={trg} => {trg2}")

