#!/usr/bin/python3

from sys import argv
from itertools import permutations

from lib.Globals import banner, repl_console, console
from lib.Functions import return_initials, generate_sentence
from lib.Functions import write_sentence, write_permutation

console.print(banner)

itertools_permutations = tuple(permutations(return_initials()))

print("Answer Y/N")
if input("Generate sentences: " + repl_console).upper() == "Y":
    generate_sentence(itertools_permutations)

if input("Write to file: " + repl_console).upper() == "Y":
    filename = input("Enter filename: " + repl_console)
    write_permutation(filename, itertools_permutations)
    write_sentence(filename, itertools_permutations)

while True:
    data = input(repl_console)
    exec(data)
