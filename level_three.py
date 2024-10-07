from settings import *
import time 
import os

def print_cat():
    for r in range(0,len(ascii_art[0])):
        os.system("clear")

        d = [] 

        for row_index in range(0,len(ascii_art)):
            d.append(ascii_art[row_index][:r])

        new_line = "\n"
        print(new_line.join(d))
        time.sleep(0.02)

if __name__ == "__main__":
    print_cat()
