# Conway's Game of life

A game where your role is to be a spectator.

The cellular automaton shows its state through a flat mesh (in this case finite) formed by squares called cells. 
Each cell has 8 neighbors, and each cell has two states: alive or dead. From there the state evolves in a sort of shifts according to 2 rules.

1. A dead cell with exactly three living neighbor cells is "born" (the next turn it will be alive).
2. A living cell with 2 or 3 living neighbor cells remains alive, but otherwise dies.
    - Cell with < 2 living neighbors dies of loneliness.
    - Cell with > 3 living neighbors dies of overpopulation.

A relatively simple, complex and beautiful game.♥️

<img align="center" src="img/Image%20homepage.png" width="500"/>

## How does it work?
**Rules**: Each square has neighbors and rules that come with number of "live" neighbors.
1. Live cell with __fewer__ than two live neighbors, then __dead cell__ caused by **loneliness**.
2. Live cell with __more__ than three live neighbors, then __dead cell__ caused by **overpopulation**.
3. Live cell with two or three live neighbors, then __live cell__
4. Live cell with three live neighbors, then __live cell__

```python
def evaluate(self):
    new_grid = copy.copy(self.grid)
        
    # Count how many neighbors are alive around of the current cell
    for row in self.grid:
        for cell in row:
            cell.count_live_neighbors()
    
    for yidx, row in enumerate(self.grid):
        for xidx, cell in enumerate(row):
            if cell.alive:
                if cell.alive_neighbors == 2 or cell.alive_neighbors == 3:
                    new_grid[yidx][xidx].alive = True
                if cell.alive_neighbors < 2 or cell.alive_neighbors > 3:
                    new_grid[yidx][xidx].alive = False
            else:
                if cell.alive_neighbors == 3:
                    new_grid[yidx][xidx].alive = True

    for yidx, row in enumerate(self.grid):
        for xidx, cell in enumerate(row):
            if cell.alive:
                new_grid[yidx][xidx].set_color()

    self.grid = new_grid
```

## Demonstration
**Steps**
1. Download this project:
   > git clone https://github.com/dimekai/Conways-Game-of-life.git

2. Create a virtual environment to have a better control.
   > python3 -m venv venv

3. Activate virtual environment 
   > source venv/bin/activate

4. Install requirements
   > pip3 install -r requirements.txt

5. Run the program
   > python3 main.py


<img align="center" src="img/Pattern%2003.png" width="500"/>
<img align="center" src="img/Pattern%2002.png" width="500"/>
<img align="center" src="img/Pattern%2001.png" width="500"/>
<br>

**Tags**: `python3` `simulation` `automata` `pygame`

