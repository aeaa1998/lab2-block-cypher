

def intInput(txt):
    while True:
        try:
            val = input(txt)
            val = int(val)
            return val
        except:
            print("Ingrese un valor númerico válido.")

def fixedInput(txt, errorTxt, size):
    while True:
        val = input(txt)
        if len(val) == size:
            return val
        else:
            print(errorTxt)


def selectOption(options, txt = "Escoja el numero de una de las siguientes opciones"):
    while True:
        for index, option in enumerate(options):
            print(index + 1, ") ", str(option))
        option = intInput(f"{txt}\n")
        if option > 0  and option <= len(options):
            return option - 1
        else:
            print("Ingrese una opcion valida")

