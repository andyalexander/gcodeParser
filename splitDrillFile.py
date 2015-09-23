__author__ = 'Andrew'
import re
import mmap


def closeString(s):
    m0 = '\nM02'
    m1 = '\nG00 Z15.0000\nM05'

    s = s.strip()

    if s.endswith('\n'):
        s = s[:-1]

    if s.endswith(m0):
        s = s[:-len(m0)]

    s += m1 + m0

    return s


def splitDrillFile(fnIn, debug):
    # fnOut = fnIn + ".ngc"

    # matchString = r"M06 \n"
    # matchString = r"G00 Z15(.*)\n(G00(.*)\n)*M06 T(.*)\nG01(.*)\nM06(.*)\n"
    # matchString = r"(G00 Z15(.*)\n(G00(.*)\n)*M06 T(.*)\nG01(.*)\nM06(.*)\n)"
    # regex = re.compile(matchString)

    print "FileName input:  " + fnIn
    # print "FileName output: " + fnOut

    f1 = open(fnIn, 'r')
    # f2 = open(fnOut, 'w')
    line = f1.readline()

    preamble = ''
    blocks = []
    sizes =[]

    blockCounter = -1

    while line != '':

        if line.startswith('M06 T'):
            blockCounter = blockCounter + 1
            blocks.append('')
            print '  Found block: {}'.format(blockCounter)

            drillSize =line.split(';', 1)[1].strip().replace('.', '-')
            sizes.append(drillSize)
            print '  -Drill size: {}mm'.format(drillSize)


            # Find the end of the block
            while line != 'M06 \n':
                line = f1.readline()

            line = f1.readline()        # read next line after the M06

        if blockCounter == -1:
           preamble = preamble + line

        else:
            blocks[blockCounter] = blocks[blockCounter] + line

        line = f1.readline()

    for i, b in enumerate(blocks):
        fnOut = fnIn + '_drill_{}mm.ngc'.format(sizes[i])
        print 'Saving file: ' + fnOut

        f2 = open(fnOut, 'w')
        f2.write(preamble + closeString(b))
        f2.close()

    f1.close()



