# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

counter = 1
while counter <= 100:
    ThreeMultiple = counter % 3 == 0
    FiveMultiple = counter % 5 == 0
    if ThreeMultiple and FiveMultiple:
        print("fizzbuzzz")
    elif ThreeMultiple:
        print("fizz")
    elif FiveMultiple:
        print("buzz")
    else:
        print(counter)
    counter += 1