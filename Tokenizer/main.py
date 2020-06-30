from chunk import run

run("program.ck")


import sys

if len(sys.argv) > 1:
    run("program_test.ck")