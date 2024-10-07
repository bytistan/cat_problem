from settings import *
import time 
import os

def print_cat():
    os.system("clear")

    for row_index,row in enumerate(ascii_art):
        for column_index, cell in enumerate(row):
            
            d = ascii_art[:row_index + 1]
            d[row_index] = ascii_art[row_index][:column_index]
            
            new_line = "\n"
            print(new_line.join(d))

            time.sleep(0.01)

            if [row_index,column_index] == [len(ascii_art) - 1,len(row) - 1]: 
                continue
            os.system("clear")

if __name__ == "__main__":
    print_cat()
