#!/usr/bin/env python3
import csv

ltrs = {'a': 2.866, 'b': 2.359, 'c': 2.532, 'd': 2.829, 'e': 2.198,
        'f': 2.158, 'g': 2.98, 'h': 2.685, 'i': 0.802, 'j': 1.949,
        'k': 2.355, 'l': 2.214, 'm': 3.607, 'n': 2.833, 'o': 3.094,
        'p': 2.413, 'q': 3.03, 'r': 2.399, 's': 2.176, 't': 2.512,
        'u': 2.748, 'v': 2.776, 'w': 4.108, 'x': 2.55, 'y': 2.596,
        'z': 2.55, '*': 0.802}

name_list = []
full_names = {}

with open('puzzle_names.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        name_list.append(row)
full_names = dict(name_list)

def calc_length(name):
    x = []
    for i in name:
        i = i.lower()
        if i in ltrs:
            x.append(ltrs.get(i))
    return sum(x) + (len(x) * 0.25)

while True:
    puzzle = input("Name: ")
    puzzle = puzzle.strip()
    if puzzle == 'q':
        break
    elif puzzle in full_names.keys():
        print(f"The exact length is {full_names.get(puzzle)} inches")
    else:
        part = (calc_length(puzzle))
        print(f"The part length is  about {part} inches")
