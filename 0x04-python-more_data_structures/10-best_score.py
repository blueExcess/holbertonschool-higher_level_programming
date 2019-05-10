#!/usr/bin/python3
def best_score(d):
    if d is None or d == {}:
        return None
    return max(d.items(), key=lambda x: x[1])[0]
