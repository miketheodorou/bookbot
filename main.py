from stats import generate_report
import sys

def main():
    args = sys.argv
    if len(args) < 2:
      print("Please provide a path to a book.")
      sys.exit(1)
    print(generate_report(args[1]))

main()