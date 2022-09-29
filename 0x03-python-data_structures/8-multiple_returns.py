#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_new = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return (tuple_new)
