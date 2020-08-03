from Crypto.Cipher import AES
from utils import selectOption, fixedInput
# Variable que contiene las posibles opciones en el menu
menu = ["Ingresar texto plano", "Leer txt", "Salir"]
# Variable que contiene las para la pregunta si o no
yesNo = ["Si", "No"]
# El default encoding que se utiliza.
encoding = 'ISO-8859-1'
# Vairbale que define si esta corriendo el programa
running = True
while running:
    # Se selecciona el la opcion del array de menu
    menuSelectedOption = selectOption(menu)
    # Se selecciono 'Ingresar texto plano'
    if menuSelectedOption == 0:
        # Se ingresa el texto que se desea cifrar
        rawString = input("Ingrese el texto que desea cifrar:\n")
        # Se ingresa la key para el cifrado ya que se uso MODE_EAX. Este modo provee autenticacion y cifrado.
        key = fixedInput("Ingrese la key para el cifrado\n", "La key debe de ser 16 caracteres de largo", 16)
        # Se instancia el cipher con el modo
        # Se debe de pasar el strin a bytes con el encoding deseado
        cipher = AES.new(key.encode(encoding).strip(), AES.MODE_EAX)
        # Es el nonce que nuestro server en este caso nuestro cipher retorna.
        # Es unico en la combinacion mensaje/key.
        nonce = cipher.nonce
        # Nuestro texto ya cifrado en bytes
        cipherString, tag = cipher.encrypt_and_digest(rawString.encode(encoding))
        # Imprimimos nuestro texto con el encoding anteriormente definido
        print("El texto cifrado es: ", cipherString.decode(encoding).strip())
        # Se revisa si se desea ver el texto decifrado
        selection = selectOption(yesNo)
        if selection == 0:
            # Vuelve a pedir la key
            key = fixedInput("Ingrese la key para el descifrado\n", "La key debe de ser 16 caracteres de largo", 16)
            # Genera una nueva instancia solo que ya definimos en nonce dentro de nuestro constructor para poder descifrar
            cipher = AES.new(key.encode(encoding).strip(), AES.MODE_EAX, nonce=nonce)
            # Se descifra el texto
            plaintext = cipher.decrypt(cipherString)
            try:
                # Si la key no hace match con el texto y el nonce rechaza la autenticación
                cipher.verify(tag)
                print("El texto descifrado es: ", plaintext.decode(encoding))
            except:
                print("Key incorrecta")
    elif menuSelectedOption == 1:
        # Se abre el archivo de donde se va a leer el texto
        readable = open("read.txt", "r")
        # Se abre el archivo de donde se va a poner el texto cifrado
        ciphereable = open("cipher.txt", "r+")
        # Se abre el archivo de donde se va a poner el texto descifrado
        desciphereable = open("deciphered.txt", "r+")
        # Se jala el texto del archivo
        rawString = readable.read()
        # Se ingresa la key para el cifrado ya que se uso MODE_EAX. Este modo provee autenticacion y cifrado.
        key = fixedInput("Ingrese la key para el cifrado\n", "La key debe de ser 16 caracteres de largo", 16)
        # Se instancia el cipher con el modo
        # Se debe de pasar el strin a bytes con el encoding deseado
        cipher = AES.new(key.encode(encoding).strip(), AES.MODE_EAX)
        # Nuestro texto ya cifrado en bytes
        nonce = cipher.nonce
        cipherString, tag = cipher.encrypt_and_digest(rawString.encode(encoding))
        print("El texto cifrado es: ", cipherString.decode(encoding).strip())
        # Se escibe el texto cifrado en nuestro archivo
        ciphereable.write(cipherString.decode(encoding).strip())
        # Se revisa si se desea ver el texto decifrado
        selection = selectOption(yesNo)
        if selection == 0:
            # Vuelve a pedir la key
            key = fixedInput("Ingrese la key para el descifrado\n", "La key debe de ser 16 caracteres de largo", 16)
            # Genera una nueva instancia solo que ya definimos en nonce dentro de nuestro constructor para poder descifrar
            cipher = AES.new(key.encode(encoding).strip(), AES.MODE_EAX, nonce=nonce)
            # Se descifra el texto
            plaintext = cipher.decrypt(cipherString)
            try:
                # Si la key no hace match con el texto y el nonce rechaza la autenticación
                cipher.verify(tag)
                print("El texto descifrado es: ", plaintext.decode(encoding))
                # Escribe dentro de nuestro archivo el texto descifrado
                desciphereable.write(plaintext.decode(encoding))
            except:
                print("Key incorrecta")

        # Se cierran los archivos
        desciphereable.close()
        ciphereable.close()
        readable.close()

    elif menuSelectedOption == 2:
        print("Gracias por usar el programa.")
        running = False


#PARTE 1
# 1) Si se utilizó ISO-8859-1 encode. Porque se tenía que pasar a bytes. Se consideró utf-8 pero nos ocurrió que ingresamos una key
#  donde había un valor no perteneciente al ascii code y fallo en el encode.
# Para cifrar el texto con este algoritmo se necesitan los bytes en si para eso sirve .encode(encoding)
# 2) Se usó EAX mode porque soporta una longitud de texto arbitrario y nos provee autenticación y cifrado.
# 3) Los parámetros fueron:
# El modo (EAX)
# El key para descifrar
# El nonce (valor random único en la relación mensaje/key)
# El texto a descifrar

#PARTE 2
# 1) Se usó EAX mode porque soporta una longitud de texto arbitrario y nos provee autenticación y cifrado. (Lo mismo que para el de arriba)
# 2) Los parámetros fueron:
# El modo (EAX)
# El key para descifrar
# El nonce (valor random único en la relación mensaje/key)
# El texto a descifrar
# 3) La key. Y el nonce son los que nos permiten la validación del cipher sin su uso no se podría pasar la autenticación.

#LINK YOUTUBE
#https://www.youtube.com/watch?v=T10qBMww_gc





