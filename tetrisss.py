import turtle
import time
import random
from typing import Set

win = turtle.Screen()
win.title("Emmanuel's Cloned Tetris Version")
win.bgcolor("white")
win.setup(width=820, height=800)
win.tracer(0)# turns off the screen update 

delay = 0.3 # to slow down the movementment of the tetrominoes

class My_shapes(): 

    def __init__(self):

        '''Has code for my blocks and their orientations
           Shapes have x and y coordinates
        
        '''
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7) #set random colours to my blocks
       
      # making a grid of 12 rows and 24 columns as per the tetris official game documentation
      
        # shapes of my blocks 
        square = [[1,1],
                  [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1,0,0,0],
                  [1,1,1,1]]
                   
        right_l = [[0,0,0,1],
                   [1,1,1,1]]
                   
        left_s = [[1,1,0],
                  [0,1,1]]
                  
        right_s = [[0,1,1],
                   [1,1,0]]
                  
        ti = [[0,1,0],
             [1,1,1]]

        My_shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, ti]

        # Choose a random shape each time
        self.shape = random.choice(My_shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])
        
        print(self.height, self.width) # for me to see the coordinates being printed as the ga

    def movement_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.clear_shapes(grid)
                self.x -= 1
        
    def movement_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.clear_shapes(grid)
                self.x += 1
    
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = self.color
              
    def clear_shapes(self, grid): #function to clear shapes or make them leave the canvas
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = 0
                  
    def can_movement(self, grid): # shapes can move
        result = True
        for x in range(self.width):
            # Check if bottom is a 1
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result
    
    def rotate(self, grid): #function to make you able to rotate shapes when the space key is pressed
        # First clear_shapes
        self.clear_shapes(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):     
            self.shape = rotated_shape
            # Update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])

# making of the grid with for loop to make it a relatively short code
grid = []
for i in range(24):
    grid.append([0]*12)

# constructing some outline for the gameplay 
outline = turtle.Turtle()
outline.pensize(10)
outline.up()
outline.hideturtle()
outline.goto(-220,246)
outline.down()
outline.color('grey')
outline.right(90)
outline.forward(490) 
outline.left(90)
outline.forward(260) 
outline.left(90)
outline.forward(490)
outline.left(90)
outline.forward(260)

#this will draw everything on the screen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid): # this function makes sure the grid is drawn anytime the game is run 
    pen.clear() # clears everything of the screen and speeds things up
    top = 232
    left = -200
     # main colours of tetrominoes from the documentation
    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]
    
    for y in range(len(grid)): # a for loop to run through the length of grids
        for x in range(len(grid[0])): # from the first grid through to the last 
            screen_x = left + (x * 20) # 20 pixels wide for each block which is the default turtle module
            screen_y = top - (y * 20)
            color_number = int(grid[y][x])
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

        

def check_grid(grid):
    # checking if each row is full or not
    global score
    
    for y in range(0,24):
        is_full = True
        y_erase = y
        for x in range(0,12):
            if grid[y][x] == 0:
                is_full = False
                break
        # Removement row and shift down
        if is_full:
            
            score += 1
            
            for y in range(y_erase-1, -1, -1):
                for x in range(0,12):
                    grid[y+1][x] = grid[y][x]

title=turtle.Turtle()
title.shape('square')
title.hideturtle()

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.score_count = 0
        self.color('white')
        self.up()
        self.hideturtle()
        self.goto(60,-300)
        self.write('Score: 0', align='center', font=('Courier', 24, 'normal'))

class Game():
    '''game class that holds most of the game functions like show start screnn and keypress on start screen'''
    def __init__(self):
        self.delay = 0.15
    
        self.win = turtle.Screen()
       
        self.win.tracer(0)
        self.win.listen()

    def show_start_screen(self): # function to allow canvas show a start screen
        self.title = Score()
        self.waiting = True
        self.title.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space') 
        
        while self.waiting:
            self.title.pencolor('red')
            self.title.write('My Cloned Tetris Game\n\n Press the "space" key to start game.\n Use arrow keys for left and right movement , \n spacebar for rotation. \n\n Re-run file to start new game' ,
                      align='center', font=('Arial', 30, 'italic'))
        self.title.clear()    
    
    def wait_for_keypress(self): # key press function to make the canvas wait until the space key is hit to run the game 
        self.waiting = False
    
   

def draw_score(pen, score):
    
    style = ('Courier', 30, 'italic')
    
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-120, 300)
    pen.write("Score:{}".format(score), move=False, align="left", font=style)


    
# this is for the 'TETRIS GAME' that appears when you play the game.

penn = turtle.Turtle()
penn.penup()
penn.speed(0)
penn.shape("square")
penn.setundobuffer(None)
def draw_name(penn, name):    
    style = ('Courier', 30, 'italic')
    penn.goto(60,100)
    penn.color("green")
    penn.hideturtle()
    penn.write("TETRIS {}\n Try as much as \n possible not to \n get to the top".format(name), move=False, align="left", font=style)


#this is to create shapes for the game to start
shape = My_shapes()

# Put the shape in the grid
grid[shape.y][shape.x] = shape.color


win.listen()
# lambda function is implemented for allowing us movement the tetrominoes..seen from the python doc and turtle doc on key press
win.onkeypress(lambda: shape.movement_left(grid), "Left")
win.onkeypress(lambda: shape.movement_right(grid), "Right")
win.onkeypress(lambda: shape.rotate(grid), "space")

# Set the score to 0
score = 0
draw_grid(pen,grid)
game=Game()
game.show_start_screen()
draw_score(pen, score)
draw_name(penn, name='GAME:')
#write_name(pen, name='Tetris')

# Main game loop
while True:
    win.update()

    if shape.y == 23 - shape.height + 1: # vertical length of the grid is height
        shape = My_shapes()
        check_grid(grid)
           
    elif shape.can_movement(grid):
      
        shape.clear_shapes(grid)
      
        shape.y +=1
        
        shape.draw_shape(grid)

    else:
        shape = My_shapes()
        check_grid(grid)

    #game.show_game_over_screen()
    draw_grid(pen,grid)
    draw_score(pen, score)
  
    time.sleep(delay)
 
win.mainloop() # keeps the canvas open for the game to continuously run
