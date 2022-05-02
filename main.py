def pulsador_nombre():
    basic.show_string("Mi Nombre Es Juan")

def pulsador_edad():
    basic.show_string("Tengo 14 años")


input.on_button_pressed(Button.A, pulsador_nombre)
input.on_button_pressed(Button.B, pulsador_edad)
