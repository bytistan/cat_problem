from settings import *

import time 
import os
import random
import shutil

class PrintCat:
    def __init__(self):
        self.new_line = "\n"
        self.interval = 0.1 
        self.columns, self.rows = shutil.get_terminal_size()

        self.pic = [
            " " * self.columns 

            for _ in range(self.rows)
        ]

        self.padding_x = ((len(self.pic[0]) - 1) - (len(ascii_art[0]) - 1)) // 2 
        self.padding_y = ((len(self.pic) - 1) - (len(ascii_art)  - 1)) // 2 
        
        self.data = [ 
            {
                "explode_location": (random.randint(0, (self.columns - 1)) ,random.randint(0, (self.rows - 1))),
                "char": char,
                "row": row_index + self.padding_y,
                "column": column_index + self.padding_x,
                "completed": False
            }

            for row_index,row in enumerate(ascii_art)
            for column_index, char in enumerate(row)
        ] 
    
        self.completed = False
        self.count = 0 
    
    def prime_factors(self, number_one, number_two):
        c = 1 
        while True:
            c += 1

            if number_one % c == 0 and number_two % c == 0: 
                return c 
            
            if c > number_one or c > number_two:
                return 1 

    def reset(self):
        self.pic = [
            " " * self.columns 

            for _ in range(self.rows)
        ]
        
        self.completed = True
        self.count = 0
        
    def setup(self):
        self.set_start_pos()
        self.print_cat()
        time.sleep(3)

    def print_cat(self): 
        image = self.new_line.join(self.pic[:-1]) + self.pic[-1]
        print(image, end="") 
        
    def set_start_pos(self):
        for index,item in enumerate(self.data):
            ep = item.get("explode_location")
            char = item.get("char")

            x, y = ep[0], ep[1]
            
            self.pic[y] = self.pic[y][:x] + char + self.pic[y][x + 1:]
    
    def update(self):
        for index,item in enumerate(self.data):
            ep = item.get("explode_location")
            char = item.get("char")

            col = item.get("column") 
            row = item.get("row")

            completed = item.get("completed") 

            x, y = ep[0], ep[1]
            
            if completed:
                self.count += 1
                self.pic[y] = self.pic[y][:x] + char + self.pic[y][x + 1:]
                continue
            
            if self.completed:
                self.completed = False 

            if x == col and y == row:
                self.data[index]["completed"] = True
            else:
                increase_rate = self.prime_factors(abs(col - x), abs(row - y))

                x_increase = -increase_rate if col < x else increase_rate 
                y_increase = -increase_rate if row < y else increase_rate 
                
                x_border, y_border = self.columns - 1, self.rows - 1 

                x += 0 if x == col else x_increase 
                y += 0 if y == row else y_increase  

                self.data[index]["explode_location"] = (x,y)

                self.pic[y] = self.pic[y][:x] + char + self.pic[y][x + 1:]

    def run(self):
        self.setup() 

        while True:
            os.system("clear")
            self.reset()
            self.update()
            self.print_cat()
            time.sleep(self.interval) 

            if self.completed:
                break

if __name__ == "__main__":
    print_cat = PrintCat()
    print_cat.run()
