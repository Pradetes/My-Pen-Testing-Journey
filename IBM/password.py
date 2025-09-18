print(" *** SISTEMA DE AUTENTICACIÓN ***")

usuario_valido = "admin"
password_valido = "1234"
max_intentos = 3
intentos = 0

while intentos < max_intentos:
    usuario_ingresado = input("Cuál es tu usuario?: ")
    password_ingresado = input("Cuál es tu password?: ")

    datos_correctos = usuario_valido == usuario_ingresado and password_valido == password_ingresado

    print(f"Datos correctos? {datos_correctos}")

    if datos_correctos:
        print("[!] Acceso concedido. Bienvenido a la plataforma")
        break
    else:
        intentos += 1
        print(f"[!] Error en la autenticación. Te quedan {max_intentos - intentos} intentos.")

if intentos == max_intentos:
    print("Demasiados intentos fallidos. Su acceso se verá bloqueado temporalmente.")
