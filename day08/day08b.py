#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
# Advent of code 2019, AoC day 8 puzzle 2
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


def represent_2d_char_list(l):
  """Output a 2d character list as aligned multiline string. Can be used for printing."""
  row_num = 0
  repres = ""
  for rowlist in l:
    if row_num > 0:
      repres += "\n"
    for c in rowlist:
      repres += str(c)
    row_num += 1
  return repres


# In[ ]:


def analyse_img(img):
  # 0=black, 1=white, 2=transparent
  layers_len = len(img)
  ylen = len(img[0])
  xlen = len(img[0][0])
  print(f"layers#={layers_len} xlen={xlen}, ylen={ylen}")
  out_img = img[0].copy()
  
  for y in range(ylen):
    for x in range(xlen):
      found_val = -1  # found pixel "color"
      for l in range(layers_len):
        val = img[l][y][x]
        out_img[y][x] = val
        if val < 2:
          break
  print(f"decoded_img list={out_img}")
  img_repr1 = represent_2d_char_list(out_img)
  print(f"decoded_img representation1=\n{img_repr1}")
  img_repr2 = img_repr1.replace('0', ' ').replace('1','#')
  print(f"decoded_img representation2=\n{img_repr2}")
  
  return 0


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


ins = '0222112222120000'
print(f"ins={ins}")
expectd = 0

test_img = build_image(ins, 2, 2)
print(f"test_img={test_img}")
res = analyse_img(test_img)

aoc.assert_msg(f"input={ins} expects output={expectd}, got {res}", expectd == res)


# In[ ]:


### personal input solution


# In[ ]:


ins = aoc.read_file_firstline_to_str("day08.in")
#print(f"{ins}")
res = solve(ins)
print(f"result={res}")
# NOTE: this shows a resulting image "font" pattern message as debug/print string


# In[ ]:





# In[ ]:




