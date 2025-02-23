import sys
from src.read_csv.read_csv import read_csv
from src.parse_args.parse_args import ParseArgs
from src.graph.graph import Graph

def parse_args(args):
    print(f"File: {args[1].split('=')[1]}")
    parsed_args = ParseArgs(args)
    data = read_csv(parsed_args.options)
    graph = Graph(parsed_args.options, data)
    graph.plot()
    print("Graphs generated successfully.")


def main():
    args = sys.argv
    if len(args) < 1:
        print("No arguments provided.")
        return
    if len(args) > 1:
        parse_args(args)

if __name__ == '__main__':
    main()