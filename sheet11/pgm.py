import io, sys

def readPGM(filename):
    d = io.open(filename, 'rb').read()
    if sys.version_info[0] > 2:
        s = ''.join([chr(k) for k in d])
    else:
        s = d
    n1 = s.find('\n')
    n2 = s.find('\n', n1+1)
    n3 = s.find('\n', n2+1)

    # check
    if s[:n1] != 'P5':
        raise ValueError("'%s' is not a valid PGM file" % filename)
    w, h, c = [int(k) for k in s[n2+1:n3].split()]
    data = [ord(k) for k in s[n3+1:]]
    return w, h, data

def writePGM(width, height, data, filename):
    s = 'P5\n# width height max_col\n%d %d %d\n' % (width, height, 255)
    import array
    if sys.version_info[0] > 2:
        t = bytes(s, "ascii") + array.array('B', data)
    else:
        t = s + array.array('B', data).tostring()
    io.open(filename, 'wb').write(t)
