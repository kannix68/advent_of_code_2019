#!/usr/bin/env python
# coding: utf-8

# In[5]:


##
# Advent of code 2019, AoC day 14 puzzle 1 and 2.
# External solution. (Used with python3.7 jupyter notebook by kannix68 @ 2020-01-07.)
#
# Discussion see [2019 Day 14 Solutions: adventofcode](https://www.reddit.com/r/adventofcode/comments/eafj32/2019_day_14_solutions/)
# this gist see https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day14.py


# In[6]:


import sys, math

def parse_input(lines):
    def _parse_numsymbol(numsymbol):
        num, symbol = numsymbol.strip().split()
        return symbol, int(num)
    reactions = {}
    for line in lines:
        left, right = line.split('=>')
        left, right = list(map(_parse_numsymbol, left.split(','))), _parse_numsymbol(right)
        reactions[right[0]] = (right[1], left)
    return reactions

def ensure(reactions, data, what, howmuch):
    if data[what] >= howmuch:
        return True
    if what == 'ORE':
        return False
    n = math.ceil((howmuch - data[what]) / reactions[what][0])
    ensured = True
    for sub_what, sub_howmuch in reactions[what][1]:
        ensured = ensured and ensure(reactions, data, sub_what, n*sub_howmuch)
        data[sub_what] -= n*sub_howmuch
    if ensured:
        data[what] += n*reactions[what][0]
    return ensured

def part1(reactions):
    low, high = 0, 10**12
    while low < high:
        mid = low + (high - low) // 2
        data = {element: 0 for element in reactions}
        data['ORE'] = mid
        if ensure(reactions, data, 'FUEL', 1):
            high = mid
        else:
            low = mid + 1
    return low

def part2(reactions):
    low, high = 0, 10**12
    while low < high-1:
        mid = low + (high - low) // 2
        data = {element: 0 for element in reactions}
        data['ORE'] = 10**12
        if ensure(reactions, data, 'FUEL', mid):
            low = mid
        else:
            high = mid - 1
    return high if ensure(reactions, data, 'FUEL', high) else low

#assert len(sys.argv) == 2
#reactions = parse_input(open(sys.argv[1]).read().split('\n'))
#
#print('Part 1: {0}, Part 2: {1}'.format(part1(reactions), part2(reactions)))


# In[7]:


#ä Modified for personal input file (name)
#assert len(sys.argv) == 2
reactions = parse_input(open("day14.in").read().strip().split('\n'))
print('Part 1: {0}, Part 2: {1}'.format(part1(reactions), part2(reactions)))

