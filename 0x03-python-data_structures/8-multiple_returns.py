#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    return length, sentence[0] if sentence else None
