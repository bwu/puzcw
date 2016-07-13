"""example.py

An example game!
"""

from puzcw import Crossword

def format_clues(clues):
    clues = map(lambda x: '%s. %s' % (x.num, x.clue), clues)
    return '\n'.join(clues)


if __name__ == "__main__":

    # Instantiate
    with open('example.puz', 'r') as f:
        puzzle = Crossword.from_str(f.read())

    # Print puzzle height and width
    print "Crossword is %sx%s" % (puzzle.width, puzzle.height)

    # Get first clue
    print puzzle.get_clue(1, 'a').clue

    # Submit first clue
    puzzle.submit(1, 'd','WORD')

    # Save puzzle
    print puzzle.save_game()