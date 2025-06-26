import sys
from checkmate import checkmate

def main():
   if len(sys.argv) == 1:
      board = """\
.....
.K...
..P..
.....
.....\
"""
      checkmate(board)
   else:
      for filename in sys.argv[1:]:
         try:
               print("Opening file:", filename)
               with open(filename, 'r') as file:
                  print("Open succeed and reading", filename)
                  content = file.read().strip()
                  checkmate(content)
                  print("Done!")
         except Exception as e:
               print("Error:", e)

if __name__ == "__main__":
    main()

