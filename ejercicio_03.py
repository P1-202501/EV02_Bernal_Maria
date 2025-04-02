import logging

logging.basicConfig(
    filename="contraseña.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def es_contraseña_valida(contraseña):
    """
    Debe tener al menos 8 caracteres, contener al menos dos números y al menos una letra mayúscula.
    """
    tiene_dos_numeros = sum(a.isdigit() for a in contraseña) >= 2
    tiene_mayuscula = any(b.isupper() for b in contraseña)
    return len(contraseña) >= 8 and tiene_dos_numeros and tiene_mayuscula

def solicitar_contraseña():
    intentos_fallidos = 0

    while True:
        contraseña = input("Crea una contraseña: ")

        if es_contraseña_valida(contraseña):
            logging.info("Contraseña válida creada.")
            print("¡Contraseña válida creada!")
            return contraseña
        else:
            logging.warning("Contraseña no válida.")
            print("Contraseña no válida. Debe tener al menos 8 caracteres, contener al menos dos números y una letra mayúscula.")
            intentos_fallidos += 1

            if intentos_fallidos == 3:
                print("No tienes mas intentos :(, terminara el programa")
                return None

def verificar_contraseña(contraseña_creada):
    intentos_fallidos = 0

    while True:
        contraseña_ingresada = input("Ingresa tu contraseña: ")

        if contraseña_ingresada == contraseña_creada:
            logging.info("Contraseña correcta.")
            print("¡Contraseña correcta!")
            break
        else:
            logging.warning("Contraseña incorrecta.")
            print("Contraseña incorrecta. Intenta nuevamente.")
            intentos_fallidos += 1

            if intentos_fallidos == 3:
                print("No tienes mas intentos :(, terminara el programa")
                break

