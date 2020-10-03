"""
Ej.5.3.a - Escribir un programa que contenga una contraseña inventada, 
que le pegunte al usuario la contraseña, y no le permita continuar
hasta que la haya ingresado correctamente.

"""
def contraseña():
    """
    Le pregunta al usuario una contraseña y no le permite continuar hasta que no la ingresa correctamente.

        Parameters:
                (str) Cadena de caracteres y números.
        
        Returns:
                (str) Cadena que indica si la contraseña es o no correcta.
    
    """
    password = "2046WKW"
    ingreso_password = input("Ingrese la contraseña:")
    
    while not password == ingreso_password:
        ingreso_password = input("Su contraseña es incorrecta, ingrese otra:")
    else:
        return print("Su contraseña es correcta.")

contraseña()