import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Lista de vocales
vocales = ["a","e","i","o","u", "á","é","í","ó","ú"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
# Menu para seleccionar la dificultad
print("-"*25)
print("Seleccione una dificultad")
print("1. Facil\n2. Media\n3. Dificil")
print("-"*25)
opcion = int(input())
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Evaluar opcion.
txt = "es :"
letters = []
if opcion == 1:
    guessed_letters += vocales
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(word_displayed)
elif opcion == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    txt = "La palabra comienza y termina de la siguiente manera: "
else:
    word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"La palabra {txt} {word_displayed}")
i = 0
while i < 10: # El programa solo fallará cuando se ingrese una letra equivocada.
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    print(letter)
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    if letter and letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
    else:
        print("Lo siento, la letra no está en la palabra.")
        i += 1
        print(f"Fallos : {i}/{max_attempts}")
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")