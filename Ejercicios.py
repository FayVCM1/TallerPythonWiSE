def prueba_for():
    for i in range(10):
        if i == 5:
            break
        print(i)

    for y in range(10):
        if y % 2 != 0:
            continue
        print(y)


# funciones
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    print(palabra)
    palabra = palabra.lower()
    print(palabra)
    palabra_inv = palabra[::-1]
    print(palabra_inv)
    if palabra == palabra_inv:
        return True
    else:
        return False
    

def pali():
    palabra = input("Escribe una palabra: ")
    validar = palindromo(palabra)
    if validar == True:
        print ("Es palindromo")
    else:
        print("No es palindromo")


# ciclos
def conteo():
    for x in range(10+1):
        print(x)


def adivina_letra():
    print("Adivina la letra secreta! \n Tienes 5 intentos.")
    intento = 0
    while intento < 5:
        letra = input("¿cual es la letra oculta?:  ")
        intento += 1
        if  letra == 'f':
            print(" Ganastes !!! ")
            break
        if intento == 5:
            print("Vuelve a intentar")


# listas
def listas():
    lista1 = [1, 2, 3]
    print(lista1)
    lista1.append('palabra')
    print(lista1)
    lista1.pop(3)
    print(lista1)
    lista1.clear()
    print(lista1)


def primo():
    numero = int(input("Escribe un numero"))
    if primo(numero):
        print("Si es un numero primo")
    else:
        print("No es un numero primo")


def sumar():
    num1 = int(input("ingrese primer numero"))
    num2 = int(input("ingrese segundo numero"))
    resultado = num1 + num2
    print(resultado)


def run():
    menu = """ 
    Bienvenido 
    digite 1 para conteo
    digite 2 para sumar
    digite 3 para """
    respuesta  = int(input(menu))
    if respuesta == 1:
        sumar()
    elif respuesta == 2:
        primo()
    elif respuesta == 3:
        listas()
    elif respuesta == 4:
        adivina_letra()
    elif respuesta == 5:
        conteo()
    elif respuesta == 6:
        pali()
    elif respuesta == 7:
        prueba_for()
    else:
        print("El usuario no ha digitado opción valida")


if __name__ ==  '__main__':
    run()
