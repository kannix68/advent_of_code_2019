import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc

import logging
logging.basicConfig(stream=sys.stdout, level=logging.WARN)
log = logging.getLogger(__name__)
log.setLevel(logging.WARN)

import itertools
import re

class Body:
  def __init__(self, pos=None, vel=None):
    self.pos = pos
    self.vel = vel
    if pos is None:
      self.pos = [0, 0, 0]
    if vel is None:
      self.vel = [0, 0, 0]

  def __repr__(self):
    return "Body"

  def __str__(self):
    return f"Body[pos={self.pos}, vel={self.vel}] E_pot={self.get_E_pot()}, E_kin={self.get_E_kin()}, E_tot={self.get_E_tot()}"

  def get_id(self):
    """Get a unique representation of body(posisition,velocity) as str."""
    return ','.join(map(str, self.pos)) + ':' + '.'.join(map(str, self.vel))

  def get_E_pot(self) -> int:
    """Get Potential Energy"""
    val = self.pos
    e = abs(val[0]) + abs(val[1]) + abs(val[2])
    return e

  def get_E_kin(self):
    """Get kinetic energy"""
    val = self.vel
    e = abs(val[0]) + abs(val[1]) + abs(val[2])
    return e

  def get_E_tot(self):
    """Get total energy"""
    return self.get_E_pot() * self.get_E_kin()
  
class NBodySystem:
  def __init__(self, tm=0, bodies=None):
    self.tm = tm
    self.bodies = bodies
    if bodies is None:
      self.bodies = []
    log.info(f"initialised {self}")

  def __repr__(self):
    return "NBodySystem"

  def __str__(self):
    return f"NBodySystem[tm={self.tm}, #bodies={len(self.bodies)}] E_pot={self.get_E_pot()}, E_kin={self.get_E_kin()}, E_tot={self.get_E_tot()}"  
  
  def get_id(self):
    return '|'.join(map(lambda b: b.get_id(), self.bodies))

  def get_bodies_str(self):
    return "\n".join(map(str, self.bodies))

  def add_body(self, b) -> None:
    self.bodies.append(b)
    log.info(f"  added {b}")

  def get_E_pot(self) -> int:
    """Get Potential Energy"""
    e = 0
    for b in self.bodies:
      e += b.get_E_pot()
    return e

  def get_E_kin(self) -> int:
    """Get kinetic energy"""
    e = 0
    for b in self.bodies:
      e += b.get_E_kin()
    return e

  def get_E_tot(self) -> int:
    """Get total energy"""
    e = 0
    for b in self.bodies:
      e += b.get_E_tot()
    return e

  def iterate_step(self) -> None:
    n_bodies = len(self.bodies)
    bodies_dv = []
    for i in range(n_bodies):
      bodies_dv.append([0, 0, 0])
    for combi in itertools.combinations(range(n_bodies), 2):
      #log.debug(f"body-idx-combi={combi}")
      idx1 = combi[0]
      idx2 = combi[1]
      b1pos = self.bodies[idx1].pos
      b2pos = self.bodies[idx2].pos
      for dimen in range(3):
        if b1pos[dimen] == b2pos[dimen]:
          a = 0
        elif b1pos[dimen] < b2pos[dimen]:
          a = 1
        elif b1pos[dimen] > b2pos[dimen]:
          a = -1
        bodies_dv[idx1][dimen] += a
        bodies_dv[idx2][dimen] -= a
      # end for dimen
    # end for combi
    log.debug(f"bodies_dv={bodies_dv}")
    for idx in range(n_bodies):
      for dimen in range(3):
        self.bodies[idx].vel[dimen] += bodies_dv[idx][dimen]
        self.bodies[idx].pos[dimen] += self.bodies[idx].vel[dimen]
    self.tm +=1
    log.info(f"nbodysystem iterated to {self}")
    for i in range(n_bodies):
      log.debug(f"  final body={self.bodies[i]}")

  def iterate(self, tm_steps=1) -> None:
    for i in range(tm_steps):
      self.iterate_step()

def get_sys_from_str(s: str):
  #log.debug(f"get_sys_from_str called with {s}")
  str_2_sys_re = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
  nbodysystem = NBodySystem()
  for line in s.split("\n"):
    m = str_2_sys_re.match(line)
    if not m:
      raise(RuntimeError(f"unparseable line {line}"))
    body_pos = list(map(int, [m.group(1), m.group(2), m.group(3)]))
    body = Body(pos=body_pos)
    log.debug(f"body={body}")
    nbodysystem.add_body(body)
  log.debug(f"nbodysystem={nbodysystem}")
  return nbodysystem