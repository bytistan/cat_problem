from settings import *
import time 
import os

def print_cat():
    # Windows 
    # os.system("cls")
    
    # Linux 
    os.system("clear")

    # Kodunu buraya yazabilirsin
    for row in ascii_art:
        print(row)
        time.sleep(0.1) 

if __name__ == "__main__":
    print_cat()

