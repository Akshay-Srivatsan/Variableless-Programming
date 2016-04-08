#!/usr/bin/env python
import copy
import sys

class Function():
    def __init__(self, line_number):
        self.line_number = line_number

    def __repr__(self):
        return "Line %d" % (self.line_number - 1)

filename = sys.argv[1]
data = []
with open(filename) as f:
    data = map(lambda x: x.strip(), f.readlines())

main_stack = []
data_stack = [[]]
line_stack = []

line_number = 1

def fix_line(line):
    if '#' in line:
        line = line[:line.find('#')]
    return line.strip().lower()


def interpret():
    global main_stack, line_stack, data_stack, line_number
    line = fix_line(data[line_number-1])


    if line == "":
        return ""

    # print "%d\t%s\t%s\t%s\t%s" % (line_number, line.replace(' ', '')[:7], main_stack, data_stack[-1], line_stack)

    if line == "exit":
        exit()
    elif line == "{":
        main_stack += [Function(line_number)]
        old_number = line_number
        while fix_line(data[line_number]) != "}":
            line_number += 1
            if line_number >= len(data):
                print "Unmatched Braces", old_number
                exit()
        line_number += 1
    elif line == "call":
        if len(main_stack) == 0:
            print "'call' requires 1 argument.", line_number
            exit()
        if main_stack[-1].__class__ != Function:
            print "'call' takes a function as its argument.", line_number
            exit()
        data_stack += [[]]
        line_stack += [line_number]
        line_number = main_stack[-1].line_number
        main_stack.pop()
    elif line == "return":
        if len(main_stack) == 0:
            print "'return' requires 1 argument.", line_number
            exit()
        line_number = line_stack.pop()
        data_stack.pop()
    elif line == "return if":
        if len(main_stack) < 2:
            print "'return if' requires 2 arguments.", line_number
            exit()
        test = main_stack.pop()
        if test:
            line_number = line_stack.pop()
            data_stack.pop()
        else:
            main_stack.pop()
    elif line == "push":
        if len(main_stack) == 0:
            print "'push' requires 1 argument.", line_number
            exit()
        data_stack[-1] += [main_stack.pop()]
    elif line == "pop":
        if len(data_stack[-1]) == 0:
            print "'pop' requires 1 value on the data stack.", line_number
            exit()
        main_stack += [data_stack[-1].pop()]
    elif line == "duplicate":
        if len(main_stack) == 0:
            print "'duplicate' requires 1 argument.", line_number
            exit()
        main_stack += [copy.copy(main_stack[-1])]
    elif line == "swap":
        if len(main_stack) < 2:
            print "'swap' requires 2 arguments.", line_number
            exit()
        main_stack[-1], main_stack[-2] = main_stack[-2], main_stack[-1]
    elif line == "less":
        if len(main_stack) < 2:
            print "'less' requires 2 arguments.", line_number
            exit()
        lesser = main_stack.pop()
        greater = main_stack.pop()
        if lesser < greater:
            main_stack += [True]
        else:
            main_stack += [False]
    elif line == "greater":
        if len(main_stack) < 2:
            print "'greater' requires 2 arguments.", line_number
            exit()
        greater = main_stack.pop()
        lesser = main_stack.pop()
        if lesser < greater:
            main_stack += [True]
        else:
            main_stack += [False]
    elif line == "discard":
        if len(main_stack) == 0:
            print "'discard' requires 1 argument.", line_number
            exit()
        main_stack.pop()
    elif line == "add":
        if len(main_stack) < 2:
            print "'add' requires 2 arguments.", line_number
            exit()
        add1 = main_stack.pop()
        add2 = main_stack.pop()
        try:
            main_stack += [add1 + add2]
        except:
            print "Cannot add '%s' and '%s'." % (add1, add2), line_number
    elif line == "negate":
        if len(main_stack) == 0:
            print "'negate' requires 1 argument.", line_number
            exit()
        arg = main_stack.pop()
        try:
            main_stack += [-1*arg]
        except:
            print "Cannot negate '%s'." % (arg), line_number
    elif line == "print":
        if len(main_stack) == 0:
            print "'print' requires 1 argument.", line_number
            exit()
        print "Output:", main_stack.pop()
    else:
        try:
            number = float(line)
            main_stack += [number]
        except ValueError:
            print "Syntax Error: Line", line_number
            print "'%s'" % line
            exit()

while True:
    result = interpret()
    if result != "jmp":
        line_number += 1
    if line_number > len(data):
        print "Unexpected End of File"
        exit()
