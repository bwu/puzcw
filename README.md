# puzcw

Puzcw gives developers an API to interact with .puz files (commonly used by NYTimes). Puzcw uses puzpy to decode .puz files and PIL to turn puzzles into images.

## Install

Install puzcw using pip.

```
sudo pip install puzcw
```

If you run into difficulties installing or using puzcw it's likely because of several development headers that are required to install the Python Imaging Library (pillow). Try installing the following:

```
libjpeg-dev
libfreetype6-dev
```

After installing the necessary headers, try reinstalling pillow.


## Library Usage
Interacting with puzcw is simple, all you need is a puzz file. Use the following example!

```
from puzcw import Crossword

# Instantiate
with open('example.puz', 'r') as f:
    puzzle = Crossword.from_str(f.read())

# Print puzzle height and width
print "Crossword is %sx%s" % (puzzle.width, puzzle.height)

# Get first clue
print puzzle.get_clue(1, 'a').clue

# Submit first answer
puzzle.submit(1, 'd','WORD')

# Save puzzle to file
print puzzle.save_game()
```