from settings import *
import time 
import os

def print_cat():
    for r in range(0,len(ascii_art[0]) + 1):
        os.system("clear")
        d = []

        for row_index,row in enumerate(ascii_art):
            if row_index % 2 == 1: 
                space = " " * (len(row) - r) if r != len(row) else ""
                d.append(space + row[-r:])
            else:
                d.append(row[:r])


        new_line = "\n"
        print(new_line.join(d))
        time.sleep(0.02)

if __name__ == "__main__":
    print_cat()
