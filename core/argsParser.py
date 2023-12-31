import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ld", type=str, help="LD name")
parser.add_argument("--rows", type=str, help="Rows index")
parser.add_argument("--cols", type=str, help="Cols index")
parser.add_argument("--resources-path", type=str, help="Resources path")
parser.add_argument("--app-storage-path", type=str, help="App Storage Path")


def getFormatedArgs():
    args = parser.parse_args()

    rows_values = args.rows.split(",")
    rowsIndex = [int(value) for value in rows_values]

    cols_values = args.cols.split(",")
    colsIndex = [int(value) for value in cols_values]

    return [args.ld, rowsIndex, colsIndex]


def getStorageConfig():
    args = parser.parse_args()
    return [args.resources_path, args.app_storage_path]
