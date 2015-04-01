def action_expected_utility(U, x, y, dx, dy):
    r = 0.7 * U[on_board(x + dx)][on_board(y + dy)]  # Expected utility of going in the intended direction
    for i in range(0, 3):
        dx, dy = rotate90(dx, dy)
        r += 0.1 * U[on_board(x + dx)][on_board(y + dy)]  # Expected utility of going in a wrong direction
    return r

def rotate90(dx, dy):  # rotates (dx, dy) 90 degrees cockwise, assuming dx, dy in {0, 1} and     dx + dy = 1
    return dy if dx == 0 else 0, -dx
    # The above expression is equivalent to the following:
    #if dx == 0 and dy == 1:
    #    return 1, 0
    #if dx == 0 and dy == -1:
    #    return -1, 0
    #if dx == 1 and dy == 0:
    #    return 0, -1
    #if dx == -1 and dy == 0:
    #    return 0, 1

def on_board(v):  # returns v if 0 <= v <= 2, else the closest of 0 and 2
    if v < 0:
        return 0
    if v > 2:
        return 2
    return v

def print_matrix(M):  # Prints the matrix in a beautiful way
    for i in range(0, len(M)):
        s = ""
        sep = ""
        for p in range(0, len(M[i])):
            s += sep + "{0:.3f}".format(M[i][p])
            sep = ", "
        print(s)

def iterate(U):  # Perform a single iteration
    U_new = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0, 3):
        for y in range(0,3):
            U_new[x][y] = reward[x][y] + gamma * max(action_expected_utility(U, x, y, 1, 0),
                                                     action_expected_utility(U, x, y, -1, 0),
                                                     action_expected_utility(U, x, y, 0, 1),
                                                     action_expected_utility(U, x, y, 0, -1))
    U_new[0][2] = 10  # Special case that must always remain 10
    return U_new

# PROGRAM START
reward = [[-0.1,-0.1,10],[-0.1,-5,-1],[-0.1,-0.1,-0.1]]
U = [[0,0,0],[0,0,0],[0,0,0]]
gamma = 0.9
for i in range(0,75):
    U = iterate(U)
print_matrix(U)


