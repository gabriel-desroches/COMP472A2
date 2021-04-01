https://github.com/gabriel-desroches/COMP472A2

# COMP472 - A2
To generate one puzzle of N by M size
```bash
$ python gen_input.py -o single_puzzle.txt 1 N M
```
To generate 20 regular puzzles
```bash
$ python gen_input.py -o analytical_inputs.txt
```
To solve puzzles using between algorithm BFS, IDS, M, H, SPI 
```bash
$ python main.py -i single_puzzle.txt -a M
```
To solve all 20 puzzles for analytical purposes
```bash
$ python analysis.py -i analytical_inputs.txt
```
