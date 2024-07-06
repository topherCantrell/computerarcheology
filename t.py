import turtle
import time

deltas = [
(-24,-16),
(0,32),
(-16,16),
(96,-32),
(-96,-32),
(16,16)
]

turtle.penup()
x=0
y=0
turtle.goto((x,y))

turtle.pendown()

for dx,dy in deltas:
  x = x + dx
  y = y + dy 
  turtle.goto((x,y))

time.sleep(5)
