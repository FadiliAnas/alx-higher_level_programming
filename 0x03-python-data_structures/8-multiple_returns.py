#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        sentence[0] = None
    first = sentence[0]
    return (length, first)
