import turtle as t
from turtle import Screen
import random
import colorgram

#colors = colorgram.extract('C:\\Users\\elanu\\OneDrive\\Desktop\\colorgram\\picture.jpg', 35)
#
#rgb_colors = []
#
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#    
#print(rgb_colors)

t.colormode(255)
color_set = [(226, 231, 236), (56, 107, 149), (225, 200, 109), (136, 86, 59), (224, 138, 59), 
             (196, 145, 171), (142, 179, 205), (138, 82, 105), (234, 226, 200), (224, 234, 230), 
             (209, 90, 70), (135, 182, 136), (69, 103, 88), (188, 78, 123), (65, 156, 88), 
             (49, 156, 196), (125, 135, 76), (238, 226, 233), (183, 192, 201), (22, 57, 89), 
             (67, 56, 45), (23, 67, 112), (216, 176, 190), (229, 174, 164), (176, 202, 182), 
             (114, 124, 148), (45, 62, 57), (112, 45, 54), (164, 204, 212), (48, 74, 69), 
             (76, 63, 49),(128, 43, 37), (9, 107, 112)]



tim = t.Turtle()
tim.penup()
tim.setheading(0)
tim.left(135)
tim.forward(300)
tim.right(135)
tim.hideturtle()

number_of_dots = 100
for dots in range(1, number_of_dots + 1):
    ran_color = random.choice(color_set)
    tim.dot(40,ran_color)
    
    if dots % 20 == 0:
        tim.setheading(270)
        tim.forward(50)
        tim.setheading(0)
    elif dots % 10 == 0:
        tim.setheading(270)
        tim.forward(50)
        tim.setheading(180)
    else:
        tim.forward(50)

    
        
        


screen = t.Screen()
screen.exitonclick()
