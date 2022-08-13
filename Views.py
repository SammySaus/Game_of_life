import States


def render(state):

    line = '--'
    for i in range(0, States.state_width(state)):
        line += '-'

    print(line)

    for i in range(0, States.state_width(state)):
        line = ''
        for j in range(0, States.state_height(state)):
            if state[i][j] == 1:
                line += '#'
            else:
                line += ' '
        print("|" + line + "|")

    line = '--'
    for i in range(0, States.state_width(state)):
        line += '-'
    print(line)
