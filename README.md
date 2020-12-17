# Sudoku-game
A colorful Sudoku game, including visualized solver.

Background and rules:
https://simple.wikipedia.org/wiki/Sudoku

**points in the design**
- This sudoku is colorful, in order to make an easy placement of a new number in a cell.
- Permanent cells are bold.
- You get an "invalid move" message when your placement doesn't follow the rules of the game.

**Before you play**
- This game was created with **pygame** package, so in order to play you must install this package.
- Run in the terminal "python sudoku_game.py" (make sure that your venv contains pygame)

**game instructions:**
- In order to type a number, choose a cell - by **left** click on it, then type your number. 0 deletes the cell content.
- In order to sketch numbers, choose a cell - by **right** click on it, then type your number. if you type a number that already typed in this cell
  it will delete it (you can sketch multiple numbers, make sure they are following the rules of he game)
- Type '**r**' -Reset board , '**s**' - Runs the visualized solver '**q**'-Quits the game  

**Solver algorithm**
- The solver was implemented using the backtracking method.
