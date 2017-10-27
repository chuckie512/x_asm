# an assembler for X, ISA from cs2410-proj1
# (c) 2017 Charles Smith <cas275@pitt.edu>

import sys

if len(sys.argv)<2:
    print '[ERROR] please specify the path of the file you wish to assemble'
    quit()

source = sys.argv[1]
dest   = 'a.x'
if len(sys.argv) >= 3:
    dest = sys.argv[2]

print '[INFO] asemling %s to %s' %(source, dest)

inf  = open(source, 'r')
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
            formt = 'R'
        elif part == 'sw':
            bn += '01001'
            formt = 'R'
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
            formt = 'R'
        elif part == 'jalr':
            bn += '10011'
            formt = 'R'
        elif part == 'j':
            bn += '11000'
            formt = 'IX'
        elif part == 'halt':
            bn += '01101'
            formt = 'R'
        elif part == 'put':
            bn += '01110'
            formt = 'R'
        else:
            print '[WARNING] UNKOWN SYMBOL %s, skipping'
        
        print '[DEBUG] %s %s %s' % (bn, formt, 'XXXX')
