from swap import swap
from argsParser import getFormatedArgs
from config import rows, cols
import sys


def getRowsAndCols(rowsIndex, colsIndex):
    selected_rows = []
    for i in range(len(rowsIndex)):
        selected_rows.append(rows[rowsIndex[i]])

    selected_cols = []
    for i in range(len(colsIndex)):
        selected_cols.append(cols[colsIndex[i]])

    return [selected_rows, selected_cols]


def main():
    [ld, rowsIndex, colsIndex] = getFormatedArgs()
    [rows, cols] = getRowsAndCols(rowsIndex, colsIndex)
    while True:
        swap(rows, cols)


if __name__ == "__main__":
    main()
