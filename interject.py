import sys

d = {}

opening = 'I\'d just like to interject for moment.'

d['<'] = ('What you\'re refering to as Linux, is in fact, GNU/Linux, or as'
          'I\'ve recently taken to calling it, GNU plus Linux.')

d['>'] = ('Linux is not an operating system unto itself, but rather another'
          ' free component of a fully functioning GNU system made useful by'
          'the GNU corelibs, shell utilities and vital system components co'
          'mprising a full OS as defined by POSIX.')

d['+'] = ('Many computer users run a modified version of the GNU system'
          'every day, without realizing it.')

d['-'] = ('Through a peculiar turn of events, the version of GNU which is'
          'widely used today is often called Linux, and many of its users are'
          'not aware that it is basically the GNU system, developed by the'
          'GNU Project.')

d['.'] = ('There really is a Linux, and these people are using it, but it is'
          'just a part of the system they use.')

d[','] = ('Linux is the kernel: the program in the system that allocates the'
          'machine\'s resources to the other programs that you run.')

d['['] = ('The kernel is an essential part of an operating system, but useless'
          'by itself; it can only function in the context of a complete'
          'operating system.')

d[']'] = ('Linux is normally used in combination with the GNU operating system'
          ': the whole system is basically'
          ' GNU with Linux added, or GNU/Linux.')

closing = ('All the so-called Linux distributions are really distributions of'
           ' GNU/Linux!')
charindex = 0
cur = 0
cell = [0 for i in range(30000)]
loops = []
dex = 0


def main():
    global dex, loops, cell, cur
    if len(sys.argv) != 2:
        raise Exception('Requires a filename')
    code = open(sys.argv[1]).read().split('\n')
    if code[0] != opening or code[-1] != closing:
        raise Exception('Invalid syntax. That is not an interject.')
    while dex != len(code):
        proc(code[dex])
        dex += 1


def proc(com):
    global out, dex, loops, cell, cur, cinput
    try:
        if com == d[">"]:
            cur += 1
            cur %= 30000
        elif com == d["<"]:
            cur -= 1
            cur %= 30000
        elif com == d["+"]:
            cell[cur] += 1
            cell[cur] %= 256
        elif com == d["-"]:
            cell[cur] -= 1
            cell[cur] %= 256
        elif com == d["."]:
            sys.stdout.write(chr(cell[cur]))
        elif com == d["["]:
            loops.append(dex)
        elif com == d[","]:
            cell[cur] = ord(input()[0])
        elif com == d["]"]:
            if cell[cur] != 0:
                dex = loops[len(loops) - 1]
            else:
                del loops[len(loops)-1]
    except Exception as e:
        raise Exception('Syntax incorrect.'
                        'Check whether or not the software is free.')
    return


main()
