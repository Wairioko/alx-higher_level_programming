#!/usr/bin/python3
for ch in range(96, 123):
    if ch != 101 & ch != 113:
        print("{:c}".format(ch), end='')
