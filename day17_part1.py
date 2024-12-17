import sys
import re
sys.setrecursionlimit(1073741824)

with open('day17_input.txt') as f:
    line = f.read().strip()
    lines = line.split('\n\n')

    rs = lines[0].split('\n')
    ra = rs[0].strip()
    a = int(re.findall('Register A: (\d+)', ra)[0])
    rb = rs[1].strip()
    b = int(re.findall('Register B: (\d+)', rb)[0])
    rc = rs[2].strip()
    c = int(re.findall('Register C: (\d+)', rc)[0])

    p = lines[1].strip()
    pm = re.findall('Program: (.*)', p)
    ops = list(map(int,pm[0].split(',')))

    def combo(operand):
        if 0<=operand<=3: return operand
        if operand == 4: return a
        if operand == 5: return b
        if operand == 6: return c
        raise Exception()

    ins = 0
    outs = []
    while ins < len(ops):
        opcode = ops[ins]
        operand = ops[ins + 1]

        if opcode == 0:
            a = a // int(2 ** combo(operand))
        if opcode == 1:
            b = b ^ operand
        if opcode == 2:
            b = combo(operand) % 8
        if opcode == 3:
            if a != 0:
                ins = operand
                continue
        if opcode == 4:
            b = b ^ c
        if opcode == 5:
            outs.append(combo(operand) % 8)
        if opcode == 6:
            b = a // int(2 ** combo(operand))
        if opcode == 7:
            c = a // int(2 ** combo(operand))

        ins += 2

    print(','.join(map(str, outs)))

