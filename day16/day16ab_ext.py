#!/usr/bin/env python
# coding: utf-8

##
# Advent of code 2019, AoC day 16 puzzles 1 and 2.
# **External solution**. (Used with python3.7 jupyter notebook by kannix68 @ 2020-01-07.)
#
# Discussion see [2019 Day 14 Solutions: adventofcode](https://www.reddit.com/r/adventofcode/comments/eafj32/2019_day_14_solutions/)
# this gist solution see https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day16.py

import sys

def get_multiplier(position, offset):
    base_pattern = [0, 1, 0, -1]
    if offset < position:
        return base_pattern[0]
    offset -= position
    return base_pattern[(offset // (position+1) + 1) % len(base_pattern)]

def part1(data):
    for _ in range(100):
        for i in range(len(data)):
            data[i] = abs(sum(data[j] * get_multiplier(i, j) for j in range(len(data)))) % 10
    return ''.join(map(str, data[:8]))

def part2(data):
    offset = int(''.join(map(str, data[:7])))
    data = (data*10000)[offset:]
    for _ in range(100):
        suffix_sum = 0
        for i in range(len(data)-1, -1, -1):
            data[i] = suffix_sum = (suffix_sum + data[i]) % 10
    return ''.join(map(str, data[:8]))

assert len(sys.argv) == 2
data = list(map(int, open(sys.argv[1]).read().strip()))

print('Part 1: {0}, Part 2: {1}'.format(part1(data[:]), part2(data[:])))
