Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.

def imprimir_numeros(n):
    if n < 0:
        return
    print(n)
    imprimir_numeros(n - 1)

# Llamamos a la función con el número inicial
imprimir_numeros(100)
