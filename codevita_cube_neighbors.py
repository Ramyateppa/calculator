import sys

n = int(sys.stdin.readline())
commands = []
existing = set()
new = set()
for _ in range(n):
    e, c, d = sys.stdin.readline().split()
    e, c = int(e), int(c)
    commands.append((e, c, d.strip().lower()))
    existing.add(e)
    new.add(c)
target = int(sys.stdin.readline())

root = list(existing - new)[0]
cube_pos = {root: (0, 0)}
pos_cube = {(0, 0): root}
move = {
    "top": (0, -1),
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

pending = commands[:]
while pending:
    remaining = []
    progressed = False
    for e, c, d in pending:
        if e not in cube_pos:
            remaining.append((e, c, d))
            continue
        x, y = cube_pos[e]
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        if (nx, ny) in pos_cube:
            old = pos_cube[(nx, ny)]
            if old != c:
                cube_pos.pop(old, None)
        if c in cube_pos:
            old_pos = cube_pos[c]
            if pos_cube.get(old_pos) == c:
                del pos_cube[old_pos]
        cube_pos[c] = (nx, ny)
        pos_cube[(nx, ny)] = c
        progressed = True
    if not progressed:
        break
    pending = remaining

if target not in cube_pos:
    ans = [-1, -1, -1, -1]
else:
    x, y = cube_pos[target]
    ans = [
        pos_cube.get((x, y - 1), -1),
        pos_cube.get((x, y + 1), -1),
        pos_cube.get((x - 1, y), -1),
        pos_cube.get((x + 1, y), -1),
    ]

# One integer per line, each followed by '\n'. No trailing spaces.
sys.stdout.write("{}\n{}\n{}\n{}\n".format(ans[0], ans[1], ans[2], ans[3]))
