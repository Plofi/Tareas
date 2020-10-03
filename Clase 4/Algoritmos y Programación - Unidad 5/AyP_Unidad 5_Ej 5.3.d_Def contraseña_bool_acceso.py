"""
Ej.5.3.d - Modificar el programa anterior para que sea una función que 
devuelva si el usuario ingresó o no la contraseña correcta, mediante un valor
booleano True o False).
"""

def contraseña_bool():
    """
    Le pregunta al usuario una contraseña y no le permite continuar 
    hasta que no la ingresa correctamente (se cierra luego de 3 intentos).
    Se agrega una pausa de tiempo de espera entre cada intento y una validación True/False.

        Parameters:
                (str) Cadena de caracteres y números.
        
        Returns:
                (str) and (bool) Cadena que indica si la contraseña es o no correcta: "Acceso: True or False", si la contraseña ingresada fue correcta o no.
                   
    """
    import time

    password = "2046WKW"
    ingreso_password = input("Ingrese la contraseña:")
    intentos = 1
    pausa = 3
    
    while not password == ingreso_password and intentos<= 3:
        acceso = False
        if intentos == 3:
            return print(f"Acceso: {acceso}. Contraseña incorrecta. Se acabaron sus intentos.")
        print(f"Acceso: {acceso}. Su contraseña es incorrecta. Tiene {3-intentos} intento/s más.")
        time.sleep(pausa)
        pausa += 3
        ingreso_password = input("Ingrese otra contraseña:")
        intentos += 1
    else:
        acceso = True
        return print(f"Acceso: {acceso}. Su contraseña es correcta.")

contraseña_bool()
