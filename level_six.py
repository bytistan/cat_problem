from settings import *
import time 
import os
import random

class PrintCat:
    def __init__(self):

        self.new_line = "\n"
        self.interval = 0.05

        self.data = [ 
            {
                "point": random.randint(0,len(ascii_art) // 2),
                "loc": 0,
                "row": len(ascii_art),
                "column":i
            }

            for i in range(len(ascii_art[0]))
        ] 
        
        self.pic = [
            " " * len(ascii_art[0])

            for _ in range(len(ascii_art))
        ]
        
        self.count = 0
    
    def reset(self):
        self.count += 1
        os.system("clear")
        self.flag = True        
    
    def print_cat(self):
        screen = self.new_line.join(self.pic)
        print(screen)

    def update(self):
        for index,item in enumerate(self.data):
            point = item.get("point")
            loc = item.get("loc")
            row = item.get("row")
            column = item.get("column")

            if point > self.count or row == 0:
                continue
            
            self.flag = False 

            if loc == row:
                self.data[index]["loc"] = 0 
                self.data[index]["row"] -= 1 
                continue
            
            self.data[index]["loc"] += 1 

            if loc not in [0,len(ascii_art)]:
                self.pic[loc - 1] = self.pic[loc - 1][:column] + " " + self.pic[loc - 1][column + 1:]
            
            self.pic[loc] = self.pic[loc][:column] + ascii_art[loc][column] + self.pic[loc][column + 1:]

    def run(self):
        while True:
            self.reset()
            self.update()
            self.print_cat()

            time.sleep(self.interval)

            if self.flag:
                break

if __name__ == "__main__":
    print_cat = PrintCat()
    print_cat.run()
