from settings import *
import time 
import os

def print_cat():
    
    flag = True
    data = {} 
    new_line = "\n"
    interval = 0.01

    for r in range(0 ,len(ascii_art[0])):
        l = ascii_art if flag else reversed(ascii_art)

        for row_index,row in enumerate(l):
            os.system("clear")
            
            data[row] = data.get(row) + row[r] if data.get(row) is not None else row[r] 

            print(new_line.join(data.values()))
            time.sleep(interval)

        flag = False if flag else True 

if __name__ == "__main__":
    print_cat()
