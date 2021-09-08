from math import sqrt
from tkinter import *
import random
from tkinter.font import BOLD


# constant  values for game 

GAME_WIDTH = 900
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PART = 3
SNAKE_COLOR = "GREEN"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "BLACK"


# variable and classes

class Snake:
    def __init__(self):
        self.body_size = BODY_PART
        self.coordinates = []
        self.squares = []


        for i in range (0, BODY_PART):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            circle = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE , fill=SNAKE_COLOR, tags="snake")
            self.squares.append(circle)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOR, tags="food")

        

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE
    
    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    #changing cooridinates, addding score and adding score 

    if  x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text=(f"Score:{score}."))

        canvas.delete("food")

        food = Food()


    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()
        quit



    windows.after(SPEED, next_turn, snake, food)
    


def change_direction(new_direction):


    global direction 

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
    



def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_WIDTH:
        print("GAME OVER")
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game over :)")
            return True
            
    
    return False   

def  game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("console", 80),text="GAME OVER :)",fill="red",
                        tags="gameover")
    


windows = Tk()
windows.title("snake game for fun")
#windows.config(bg="black")
windows.resizable(False, False)

score = 0
direction = "down"
label = Label(windows, text= "score:{}".format(score), 
            font=("console", 45))
label.pack()

canvas = Canvas(windows, background=BACKGROUND_COLOR, height=GAME_HEIGHT,
                width=GAME_WIDTH)
canvas.pack()
windows.update()


#rendering for canvas

windows_width = windows.winfo_width()
windows_height = windows.winfo_height()
screen_width = windows.winfo_width()
screen_height = windows.winfo_height()

x = int((screen_width/2) - (screen_width/2))
y = int((screen_height/2) - (screen_height/2))

windows.geometry(f"{windows_width}x{windows_height}+{x}+{y}")

#control to manage snake

windows.bind("<Left>", lambda event: change_direction("left"))
windows.bind("<Right>", lambda event: change_direction("right"))
windows.bind("<Up>", lambda event: change_direction("up"))
windows.bind("<Down>", lambda event: change_direction("down"))




snake = Snake()
food = Food()
next_turn(snake, food)




windows.mainloop()