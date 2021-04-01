https://github.com/gabriel-desroches/COMP472A2

# COMP472 - A2

Completed By:  
Gabriel Desroches  
Felix Morin  
Richard Nguyen  
Vladislav Voznitsa  

**To generate puzzle of N by M size**
```bash
usage: analysis.py [-h] -i FILENAME

Generate an analysis over S-Puzzle games for all different search algorithms

optional arguments:
  -h, --help   show this help message and exit
  -i FILENAME  filename of the puzzles
```
Example for one puzzle of size 3 by 4
```bash
$ python gen_input.py -o single_puzzle.txt 1 3 4
```
Example for 20 regular puzzles
```bash
$ python gen_input.py -o analytical_inputs.txt
```
**To solve puzzles using between algorithm BFS, IDS, M, H, SPI**
```bash
usage: Main.py [-h] -i FILENAME -a ALGORITHM

S-Puzzle game which finds a solution for each puzzles in the selected file given the different search algorithms

optional arguments:
  -h, --help    show this help message and exit
  -i FILENAME   filename of the puzzles
  -a ALGORITHM  search algorithms (DFS, IDS, M, SPI, H)
```
Example of solving 1 puzzle using Manhattan algorithm
```bash
$ python main.py -i single_puzzle.txt -a M
```
**To solve all 20 puzzles for analytical purposes**
```bash
usage: Main.py [-h] -i FILENAME -a ALGORITHM

S-Puzzle game which finds a solution for each puzzles in the selected file given the different search algorithms

optional arguments:
  -h, --help    show this help message and exit
  -i FILENAME   filename of the puzzles
  -a ALGORITHM  search algorithms (DFS, IDS, M, SPI, H)
```
Example
```bash
$ python analysis.py -i analytical_inputs.txt
```
