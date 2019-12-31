#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 8 puzzle 1
# This solution (python3.7 jupyter notebook) by kannix68, @ 2019-12-31.

import sys
sys.path.insert(0, '..')  # allow import from parent dir
import lib.aochelper as aoc


# In[ ]:


## PROBLEM DOMAIN code


# In[ ]:


# flatten a list
# see [python - How to make a flat list out of list of lists? - Stack Overflow](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)
# flatten = lambda l: [item for sublist in l for item in sublist]
def flatten(l):
  """Flatten an arbitrary list-of-lists into one flat list."""
  return [item for sublist in l for item in sublist]


# In[ ]:


def build_image(s, layer_width, layer_height):
  layer_size = layer_width * layer_height
  stp = 0
  l = 0
  x = 0
  y = 0
  img = []
  cur_layer = []
  cur_row = []
  for i in map(int, s):
    if 0 == stp % layer_size and stp > 0:  # new layer
      #print(f"stp={stp}, new layer")
      l += 1
      x = 0
      y = 0
      cur_layer.append(cur_row)
      img.append(cur_layer)
      cur_layer = []
      cur_row = []
    else:
      if 0 == stp % layer_width and stp > 0:  # new row
        #print(f"stp={stp}, new row")
        y += 1
        x = 0
        cur_layer.append(cur_row)
        cur_row = []
    cur_row.append(i)
    #print(f"  stp={stp} appended {i} at pos={x,y} in layer={l}")
    stp += 1
    x += 1
  cur_layer.append(cur_row)
  img.append(cur_layer)
  #print(f"img={img}")
  return img


# In[ ]:


def analyse_img(img):
  flat_layers = list(map(flatten, img))
  #print(f"flattened layers={list(flat_layers)}")
  num_zeros = list(map(lambda l: len(list(filter(lambda i: i == 0, l))), flat_layers))
  print(f"num_0s list={num_zeros}")

  # see [Python: Find index of minimum item in list of floats - Stack Overflow](https://stackoverflow.com/questions/13300962/python-find-index-of-minimum-item-in-list-of-floats)
  val, idx = min((val, idx) for (idx, val) in enumerate(num_zeros))

  print(f"min 0s layer idx#={idx} val={val}")
  target_layer = flat_layers[idx]
  #print(f"target layer={target_layer}")

  num_layer_1s = len(list(filter(lambda i: i == 1, target_layer)))
  num_layer_2s = len(list(filter(lambda i: i == 2, target_layer)))
  prod = num_layer_1s * num_layer_2s
  print(f"#_1s={num_layer_1s} #_2s={num_layer_2s}; product={prod}")
  
  return prod


# In[ ]:


def solve(inputs):
  layer_width = 25
  layer_height = 6
  return analyse_img(build_image(inputs, layer_width, layer_height))


# In[ ]:


## MAIN


# In[ ]:


### tests


# In[ ]:


ins = '123456789012'
print(f"ins={ins}")
expectd = 1

test_img = build_image(ins, 3, 2)
res = analyse_img(test_img)

aoc.assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)


# In[ ]:


### personal input solution


# In[ ]:


ins = aoc.read_file_firstline_to_str("day08.in")
#print(f"{ins}")
res = solve(ins)
print(f"result={res}")

