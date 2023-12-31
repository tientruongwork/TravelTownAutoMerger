from multiprocessing import Process
from swap import swap
from config import rows, cols


def main(selectedRowsIndex, selectedColsIndex):
    selected_rows = []
    for i in range(len(selectedRowsIndex)):
        selected_rows.append(rows[selectedRowsIndex[i]])

    selected_cols = []
    for i in range(len(selectedColsIndex)):
        selected_cols.append(cols[selectedColsIndex[i]])

    print(selected_rows, selected_cols)
    while True:
        try:
            swap(selected_rows, selected_cols)
        except:
            pass


# Define a global variable
program_process = None


def reset_program_process(rows, cols):
    global program_process
    program_process = Process(target=main, args=(rows, cols))
    return program_process


def get_program_process():
    return program_process
