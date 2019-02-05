#################

not_in documentation

author:	Jae Chan Hwang (hwangjc@umich.edu)
date:	10-16-2018

#################

usage: not_in.py [-h] -a A -b B [-o OUTPUT]

Simple script that gets all lines in file a but are not in file b. Essentially
a set subtract A - B.

optional arguments:
  -h, --help            show this help message and exit
  -a A                  The name of file a.
  -b B                  The name of file b.
  -o OUTPUT, --output OUTPUT
                        The name of the file to output to. Will print to
                        stdout if none specified.

examples:

	file a:
		apple
		apple
		orange
		banana

	file b:
		orange
		grape

	output:
		apple
		banana
