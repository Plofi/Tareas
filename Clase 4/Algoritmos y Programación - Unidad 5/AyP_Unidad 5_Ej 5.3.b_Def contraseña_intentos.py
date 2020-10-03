"""
Ej.5.3.b - Modificar el programa anterior para que solamente
permita una cantidad fija de intentos.

"""
def contraseña_intentos():
    """
    Le pregunta al usuario una contraseña y no le permite continuar 
    hasta que no la ingresa correctamente (se cierra luego de 3 intentos).

        Parameters:
                (str) Cadena de caracteres y números.
        
        Returns:
                (str) Cadena que indica si la contraseña es o no correcta.
    
    """
    password = "2046WKW"
    ingreso_password = input("Ingrese la contraseña:")
    intentos = 1
    while not password == ingreso_password and intentos<= 3:
        if intentos == 3:
            return print("Contraseña incorrecta. Se acabaron sus intentos.")
        ingreso_password = input(f"Su contraseña es incorrecta, tiene {3-intentos} intento/s más, ingrese otra contraseña:")
        intentos += 1
    else:
        return print("Su contraseña es correcta.")

contraseña_intentos()