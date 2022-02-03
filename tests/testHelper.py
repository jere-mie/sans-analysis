def updatePath():
    import sys
    from pathlib import Path
    sys.path.append(str(Path('.').absolute()))

    # the following goes one directory higher than the above line
    # sys.path.append(str(Path('.').absolute().parent))

# this is useful with assert statements using floats
def almost_equals(a, b):
    return abs(a-b) < 0.0001