from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Scoreboard
from  snake import Snake


from snake import Snake

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
sleep_time = 0.1
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(sleep_time)

    snake.move()

    #Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_score()
        sleep_time -= 0.001
        time.sleep(sleep_time)

    #Detect Collision With Wall
    if snake.head.xcor() > 420 or snake.head.xcor() < -420 or snake.head.ycor() > 420 or snake.head.ycor() < -420:
        scoreboard.reset()
        snake.reset()

    #Detect Collision With Tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()