#!/usr/local/bin/python

import argparse

def get_parser():
    """Gets parser"""
    parser = argparse.ArgumentParser(description="Cry for help calling a name")
    parser.add_argument('name', help="The name of the saviour")
    return parser.parse_args()

def main():
    p = get_parser()
    print "Help me, {0}".format(p.name)

if __name__ == "__main__":
    main()
