import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N',  nargs='+')
args = parser.parse_args()

print(args)
