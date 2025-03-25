import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
puntaje = 0
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
for question, answer_options, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: ")) - 1
        # Se verifica si la respuesta es correcta
        if user_answer in correct_answers_index:
            if user_answer == correct_index:
                print("¡Correcto!")
                puntaje += 1
                break
            else:
                # Si el usuario no responde correctamente después de 2 intentos,
                # se muestra la respuesta correcta
                print("Incorrecto. La respuesta correcta es:")
                print(answer_options[correct_index])
                puntaje -= 0.5
        else:
            print(f"Respuesta no válida")
            sys.exit(1)
    # Se imprime un blanco al final de la pregunta
    print()
    print(f"Resultado:{puntaje}")