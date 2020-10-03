"""
Ej.5.3.c - Modificar el programa anterior para que desués de cada intento
agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.

"""

def contraseña_intentos_sleep():
    """
    Le pregunta al usuario una contraseña y no le permite continuar 
    hasta que no la ingresa correctamente (se cierra luego de 3 intentos).
    Se agrega una pausa de tiempo de espera entre cada intento.

        Parameters:
                (str) Cadena de caracteres y números.
        
        Returns:
                (str) Cadena que indica si la contraseña es o no correcta.
    
    """
    import time

    password = "2046WKW"
    ingreso_password = input("Ingrese la contraseña:")
    intentos = 1
    pausa = 3

    while not password == ingreso_password and intentos<= 3:
        if intentos == 3:
            return print("Contraseña incorrecta. Se acabaron sus intentos.")
        print(f"Su contraseña es incorrecta, tiene {3-intentos} intento/s más.")
        time.sleep(pausa)
        pausa += 3
        ingreso_password = input("Ingrese otra contraseña:")
        intentos += 1
    else:
        return print("Su contraseña es correcta.")

contraseña_intentos_sleep()