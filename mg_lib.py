# Music Generator Library

def major_chord(root):
    return [root, root + 4, root + 7]

def minor_chord(root):
    return [root, root + 3, root + 7]

def major_scale(root):
    res = [root]
    for i in range(6):
        if (i != 2):
            res.append(res[len(res) - 1] + 2)
        else:
            res.append(res[len(res) - 1] + 1)
    return res