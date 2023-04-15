import turtle
import random
import time

# Crear la ventana para la carrera
window = turtle.Screen()
window.title("Carrera de Tortugas")

# Esperar 5 segundos antes de iniciar la carrera
time.sleep(10)

# Configurar la forma y color de las tortugas
turtle_shape = "turtle"
tortuga1_color = "red"
tortuga2_color = "blue"

# Crear dos tortugas
tortuga1 = turtle.Turtle(shape=turtle_shape)
tortuga1.color(tortuga1_color)

tortuga2 = turtle.Turtle(shape=turtle_shape)
tortuga2.color(tortuga2_color)

# Configurar la posición inicial de las tortugas
tortuga1.penup()
tortuga1.goto(-200, 20)
tortuga1.pendown()

tortuga2.penup()
tortuga2.goto(-200, -20)
tortuga2.pendown()

# Carrera
for i in range(150):
    # Mover las tortugas en una dirección aleatoria
    tortuga1.forward(random.randint(1, 5))
    tortuga2.forward(random.randint(1, 5))

# Esperar a que el usuario cierre la ventana
turtle.done()
