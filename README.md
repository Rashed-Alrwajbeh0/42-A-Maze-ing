*This activity has been created as part of the 42 curriculum by abdothma, ralrawaj.*

# A-Maze-ing

## Description

A-Maze-ing is a maze generation project developed in Python.

The goal of this project is to generate valid random mazes from a configuration file, export them using a hexadecimal wall representation, and provide a visual representation of the generated maze.

The application supports:

- Random maze generation
- Reproducible generation through seeds
- Perfect mazes (single valid path between entry and exit)
- Shortest path calculation
- Maze export to a file
- Terminal visualization
- Displaying and hiding the solution path
- Custom wall colors
- Reusable maze generation package

---

# Features

- Generate mazes of arbitrary dimensions
- Support for perfect and non-perfect mazes
- Configurable entry and exit points
- Deterministic generation using seeds
- Hexadecimal wall encoding
- Automatic shortest path generation
- ASCII terminal renderer
- Color customization
- Reusable MazeGenerator package

---

# Instructions

## Requirements

- Python 3.10+
- pip
- Make

## Running

```bash
python3 a_maze_ing.py config.txt
```

or

```bash
make run
```

## Debug Mode

```bash
make debug
```

## Linting

```bash
make lint
```

Optional strict linting:

```bash
make lint-strict
```

## Cleaning Cache Files

```bash
make clean
```

---

# Configuration File Format

The configuration file uses one `KEY=VALUE` pair per line.

Example:

```txt
# Maze dimensions
WIDTH=20
HEIGHT=15

# Entry and exit coordinates
ENTRY=0,0
EXIT=19,14

# Output file
OUTPUT_FILE=maze.txt

# Perfect maze
PERFECT=True

# Optional
SEED=42
```

## Available Keys

| Key | Description |
|-------|-------------|
| WIDTH | Maze width |
| HEIGHT | Maze height |
| ENTRY | Entry coordinates |
| EXIT | Exit coordinates |
| OUTPUT_FILE | Output file name |
| PERFECT | Generate a perfect maze |
| SEED | Random seed (optional) |

---

# Maze Generation Algorithm

## Selected Algorithm

Recursive Backtracker (Depth-First Search)

### How It Works

1. Start from a random cell.
2. Mark it as visited.
3. Randomly choose an unvisited neighbor.
4. Remove the wall between the cells.
5. Continue recursively until all cells are visited.
6. Backtrack whenever no unvisited neighbors remain.

### Why This Algorithm

The Recursive Backtracker was chosen because:

- Easy to implement
- Produces perfect mazes naturally
- Fast for medium and large mazes
- Creates long and interesting corridors
- Low memory requirements

---

# Output File Format

Each maze cell is represented by a hexadecimal digit.

Wall encoding:

| Bit | Direction |
|-------|-----------|
| 0 | North |
| 1 | East |
| 2 | South |
| 3 | West |

Example:

```txt
FA98
8123
1E4A

0,0
19,14
EESSEENNWWSS
```

The file contains:

1. Maze data
2. Entry coordinates
3. Exit coordinates
4. Shortest valid path

---

# Reusable Module

The reusable part of this project is the `MazeGenerator` package.

## Basic Usage

```python
from mazegen import MazeGenerator

generator = MazeGenerator(
    width=20,
    height=15,
    seed=42,
    perfect=True
)

maze = generator.generate()
```

## Access Maze Data

```python
maze = generator.maze
```

## Retrieve Solution

```python
path = generator.shortest_path()
```

## Build Package

```bash
python -m build
```

Example output:

```txt
dist/
├── mazegen-1.0.0.tar.gz
└── mazegen-1.0.0-py3-none-any.whl
```

---

# Project Structure

```txt
.
├── a_maze_ing.py
├── config.txt
├── maze/
│   ├── generator.py
│   ├── parser.py
│   ├── solver.py
│   └── renderer.py
├── dist/
├── README.md
├── Makefile
└── pyproject.toml
```

---

# Team & Project Management

## Team Members

### abdothma

Role:
- Imperfect maze
- BFS algorithm
- Colorizing maze
- Makefile
- README.md
- Documentation

### Team Member 2

Role:
- Perfect Maze
- Reading config.txt
- writing output
- Maze printing
- User interactions
- flake8
- mypy

---

## Tools Used

- Python
- Git
- Make
- mypy
- flake8
- pytest
- ChatGPT
- VS Code

---

# AI Usage

AI tools were used for:

- Documentation drafting
- Code reviews
- Algorithm research
- Type hint validation
- README formatting

All generated content was reviewed, tested, and understood before integration.

---

# Resources

- wikipedia
- google

---
