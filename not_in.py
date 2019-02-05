import sys
import argparse
import cStringIO


##### parse arguments
parser = argparse.ArgumentParser(description="Simple script that gets all lines in file a but are not in file b. Essentially a set subtract A - B.")
parser.add_argument('-a', required=True, help="The name of file a.")
parser.add_argument('-b', required=True, help="The name of file b.")
parser.add_argument('-o', '--output', required=False, help="The name of the file to output to. Will print to stdout if none specified.")

_args = parser.parse_args()
globals()['args'] = _args
#####

##### ___main___ #####

if args.a == args.output or args.b == args.output:
    print("Input and output cannot be the same file")
    sys.exit()

file_a = open(args.a, 'r')
file_b = open(args.b, 'r')

if args.output != None:
    file_output = open(args.output, "w")

lines_in_a = set()
lines_in_b = set()

for line in file_a:
    lines_in_a.add(line)

for line in file_b:
    lines_in_b.add(line)

diff = lines_in_a - lines_in_b

for each in diff:
    if args.output != None:
        file_output.write(each) 
    else:
        print(each)

##### end #####
