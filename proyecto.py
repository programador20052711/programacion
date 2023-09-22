from turtle import* 
import colorsys
import math 
import random
# Configuración de la pantalla
wn = Screen()
wn.bgcolor("black")

# Función para dibujar una estrella
def draw_star(x, y):
    up()
    goto(x, y)
    down()

    color("purple")
    begin_fill()
    for _ in range(5):
        forward(20)
        right(144)

    end_fill()

# Dibuja varias estrellas en ubicaciones aleatorias
for _ in range(15):
    speed(20)
    x = random.randint(-700, 300)
    y = random.randint(200, 300)


    draw_star(x, y)
    #color de otras estrellas
def draw_star(g,z):
    up()
    goto(g,z)
    down()

    color("yellow")
    begin_fill()
    for _ in range(5):
        forward(20)
        right(144)

    end_fill()
#dibuja otras estrellas en ubicacion aleatorias 
for _ in range(15):
    speed(20)
    g = random.randint(-700, 300)
    z = random.randint(200, 300)
    
    
    draw_star(g,z)
    #color de otras estrellas
def draw_star(s,t):
    up()
    goto(s,t)
    down()

    color("white")
    begin_fill()
    for _ in range(5):
        forward(20)
        right(144)

    end_fill()
#dibujar otras estrellas en ubicacion aleatorias 
for _ in range(15):
    speed(20)
    s = random.randint(-700,300)
    t = random.randint(200,300)
    draw_star( s,t)
#se va hacer la configuracion inicial
shape("turtle")
speed(20)
#dibujar ahora el tallo
penup()
goto(10,-350)
pendown()
color("light green")
begin_fill()
left(90)
forward(300)
left ( 90)
forward(30)
left(90)
forward(300)
left(90)
forward(30)
end_fill()
#escribir un mensaje hermoso
penup()
goto( -30, -200)# ajuste de la posicion donde estara ubicado el texto
color("pink") # color del texto de la letra 
write("para esa futbolista, que algun dia cumplira toda sus metas ",align="center",font=("arial",5, "bold"))
penup()
goto(-30,-250)# ajuste de la posicion abajo del otro texto
color("pink")
write("eres una de las personas maravillosas que tengo alrededo ",align="center",font=("arial",5, "bold"))
goto(-30,-300)# ajuste de la posicion abajo del otro texto
color("pink")
write("nunca dudes de lo que puedes hacer actualmente y lo que podras hacer en el futuro. ",align="center",font=("arial",5, "bold"))

# Mueve la pluma a la posición donde deseas dibujar el corazón
penup()
goto(450, -200)  # Cambia las coordenadas según tus preferencias
pendown()

# Configura el relleno del corazón
fillcolor("red")
begin_fill()
pensize(1)

# Dibuja la mitad izquierda del corazón
left(140)
forward(40)
for _ in range(200):
    right(1)
    forward(0.3)

# Dibuja la mitad derecha del corazón
left(120)
for _ in range(200):
    right(1)
    forward(0.3)

# Completa el corazón
forward(40)

# Finaliza el relleno del corazón
end_fill()
#color para el medio del girasol (RGB:139, 69, 19) 
penup()
goto(0,-200)
fillcolor("#0000FF")
begin_fill()
circle(0,0)
end_fill()
angulo= 137.508 * (math.pi/ 180.0)
for i in range(180 + 50):
    radio = 4 * math.sqrt(i)
    forma = i * angulo
    x = radio * math.cos(forma)
    y = radio*math.sin(forma)
    penup()
    goto(x,y)
    setheading(i * 137.510)
    pendown()
    if i < 180:
        stamp()
    else:
        fillcolor("white")
        begin_fill()
        circle(90,85)
        left(90)
        end_fill()            
#ocultar el cursor de la tortuga antes de salir 
hideturtle()
#cerrar la ventana al hacer click 
exitonclick()






       
        

    
    


    

