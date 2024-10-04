#triangle
#import turtle
#s = turtle.getscreen()
#t = turtle.Turtle()
#t.speed(0) # maximum speed
#def equilateral(longeur):
#    for _ in range(3):
#        t.forward(longeur)
#        t.left(120)
#
#equilateral(100)
#turtle.exitonclick()

#carre
#import turtle
#s = turtle.getscreen()
#t = turtle.Turtle()
#t.speed(0) # maximum speed
#def equilateral(longeur):
#    for _ in range(4):
#        t.forward(longeur)
#        t.left(90)

#equilateral(100)
#turtle.exitonclick()

#exagone
#import turtle
#s = turtle.getscreen()
#t = turtle.Turtle()
#t.speed(0) # maximum speed
#def equilateral(longeur):
#    for _ in range(5):
#        t.forward(longeur)
#        t.left(72)

#equilateral(100)
#def equilatera(longeur):
#    for _ in range(5):
#        t.forward(longeur)
#        t.left(72)
        
#equilatera(50)
#turtle.exitonclick()


#import turtle
#s = turtle.getscreen()
#t = turtle.Turtle()
#t.speed(0) # maximum speed
#def equilateral(longeur):
#    for _ in range(30):
#        t.forward(longeur)
#        t.right(60)

#equilateral(100)
#def equilatera(longeur):
#    for _ in range(30):
#        t.forward(longeur)
#        t.right(60)
        
#equilatera(150)  
#turtle.exitonclick()

#import turtle
#s = turtle.getscreen()
#t = turtle.Turtle()

#def etoile(k,h):
#    t.color ("orange")
#    for _ in range (k):
#        t.forward(200)
#        t.right(360*h/k)
        
#etoile(130 , 70)



#import turtle

#t = turtle.Turtle()

# Cycler une liste de couleurs
#for c in ['red', 'green', 'yellow', 'blue']: # rougen vert, jaune, bleu 
#    t.color(c)    # Fixer la couleur
    
#    t.forward(75) # Avancer
#    t.left(90)



#import turtle

#t = turtle.Turtle()

#def faire_carre():
#  for i in range( 4 ):
#      for c in ['red', 'green', 'turquoise', 'purple']:  
#          t.color(c)
#          t.forward( 100 )
#          t.right(90)

#def faire_fleur():
#  angle = 5 # en degrés
#  for i in range( 360 // angle ):
#    faire_carre()
#    t.left( angle )

#t.clear()
#faire_fleur()


from turtle import *
color('turquoise', 'purple')
begin_fill()
while True:
    forward(200)
    left(170)
    if (abs(pos()[0]) < 1) and (abs(pos()[1]) < 1) :
        break
        print( "break")
end_fill()
done()