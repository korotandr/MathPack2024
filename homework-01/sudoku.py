import pathlib
import typing as tp
import numpy as np

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """Сгруппировать значения values в список, состоящий из списков по n элементов""" 
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[i * n + j])
        matrix.append(row)
    return matrix

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""
    return grid[pos[0]]

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""
    col = []
    for i in range(len(grid)):
        col.append(grid[i][pos[1]])
    return col

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    block = []
    start_i = pos[0]//3 * 3
    end_i = pos[0]//3 * 3 + 3
    start_j = pos[1]//3 * 3
    end_j = pos[1]//3 * 3 + 3
    for i in range(start_i, end_i):
        for j in range(start_j, end_j):
            block.append(grid[i][j])

    return block

def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)
    return False

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции"""
    possible_values = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    values = set(get_block(grid, pos) + get_row(grid, pos) + get_col(grid, pos))
    return possible_values - values

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    if find_empty_positions(grid) == False:
        return grid
    else:
        pos = find_empty_positions(grid)
        values = find_possible_values(grid, pos)
        solution = "Нет решения"
        while len(values) != 0:
            grid[pos[0]][pos[1]] = values.pop()
            solution = solve(grid)
            if type(solution) is list:
                break
            else:
                grid[pos[0]][pos[1]] = '.'
        return solution

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    correct = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    for i in range(0, len(solution), len(solution) // 3):
        if set(get_block(solution, [i, i])) != correct:
            return False
        
    for i in range(len(solution)):
        if set(get_row(solution, [i, 0])) != correct:
            return False
        
        if set(get_row(solution, [0, i])) != correct:
            return False
        
        return True

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    
    pass

if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt", "puzzlemax.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)