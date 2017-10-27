#!/usr/bin/env python
# an assembler for X, ISA from cs2410-proj1
# (c) 2017 Charles Smith <cas275@pitt.edu>

import sys

if len(sys.argv)< 3:
    print '[ERROR] please specify the path of the file you wish to assemble'
    quit()

source = sys.argv[1]
dest   = 'a.x'
if len(sys.argv) >= 3:
    dest = sys.argv[2]

print '[INFO] asemling %s to %s' %(source, dest)

inf = open(source, 'r')
outf = open(dest, 'w')

for line in inf:
    if line[0] != '#':
        #not a comment

        bn = ''
        formt = ''

        line.replace(',', ' ')
        # figuring out which instruction we have
        part = (line.split()[0]).lower()
        if part == 'add':
            bn += '00000'
            formt = 'R'
        elif part == 'sub':
            bn += '00001'
            formt = 'R'
        elif part == 'and':
            bn += '00010'
            formt = 'R'
        elif part == 'nor':
            bn += '00011'
            formt = 'R'
        elif part == 'div':
            bn += '00100'
            formt = 'R'
        elif part == 'mul':
            bn += '00101'
            formt = 'R'
        elif part == 'mod':
            bn += '00110'
            formt = 'R'
        elif part == 'exp':
            bn += '00111'
            formt = 'R'
        elif part == 'lw':
            bn += '01000'
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "{0:03b}".format(int(line.split()[2][1]))
            bn += "00000"

        elif part == 'sw':
            bn += '01001'
            bn += '000'
            bn += "{0:03b}".format(int(line.split()[2][1]))
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "00"

        elif part == 'liz':
            bn += '10000'
            formt = 'I'
        elif part == 'lis':
            bn += '10001'
            formt = 'I'
        elif part == 'lui':
            bn += '10010'
            formt = 'I'
        elif part == 'bp':
            bn += '10100'
            formt = 'I'
        elif part == 'bn':
            bn += '10101'
            formt = 'I'
        elif part == 'bx':
            bn += '10110'
            formt = 'I'
        elif part == 'bz':
            bn += '10111'
            formt = 'I'
        elif part == 'jr':
            bn += '01100'
            bn += "000"
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "00000"

        elif part == 'jalr':
            bn += '10011'
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "{0:03b}".format(int(line.split()[2][1]))
            bn += "00000"

        elif part == 'j':
            bn += '11000'
            bn += "{0:011b}".format(int(line.split()[1]))

        elif part == 'halt':
            bn += '01101'
            bn += "00000000000"

        elif part == 'put':
            bn += '01110'
            bn += "000"
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "00000"

        else:
            print '[WARNING] UNKOWN SYMBOL %s, skipping'

        if formt == 'R':
            bn += "{0:03b}".format(int(line.split()[1][1]))
            bn += "{0:03b}".format(int(line.split()[2][1]))
            bn += "{0:03b}".format(int(line.split()[3][1]))
            bn += "00"

        if formt == 'I':
            bn += '{0:03b}'.format(int(line.split()[1][1]))
            if int(line.split()[2]) < 0:
                print "converting"
                temp = int(line.split()[2])
                temp = pow(2, 8) + temp
                bn += "{0:08b}".format(temp)

            else:
                bn += "{0:08b}".format(int(line.split()[2]))

        hexOut = "{0:0>4X}".format(int(bn, 2))
        print '[DEBUG] %s %s' % (bn, hexOut)

        outf.write(hexOut + '\n')
