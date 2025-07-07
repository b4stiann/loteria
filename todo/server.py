from flask import Flask, render_template
import random

app = Flask(__name__)

#Lista es de cartas para el nivel 4 

cartas = [
    "1ElGallo", "2ElDiablito", "3LaDama", "4Elcatrín", "5Elparaguas", "6Lasirena", "7Laescalera",
    "8Labotella", "9Elbarril", "10Elárbol", "11Elmelón", "12Elvaliente", "13Elgorrito", "14Lamuerte", "15Lapera",
    "16Labandera", "17Elbandolón", "18Elvioloncello", "19Lagarza", "20Elpájaro", "21Lamano", "22Labota",
    "23Laluna", "24Elcotorro", "25Elborracho", "26Elnegrito", "27Elcorazón", "28Lasandía", "29Eltambor",
    "30Elcamarón", "31Lasjaras", "32Elmúsico", "33Laraña", "34Elsoldado", "35Laestrella", "36Elcazo",
    "37Elmundo", "38Elapache", "39Elnopal", "40Elalacrán", "41Larosa", "42Lacalavera", "43Lacampana",
    "44Elcantarito", "45Elvenado", "46Elsol", "47Lacorona", "48Lachalupa", "49Elpino", "50Elpescado",
    "51Lapalma", "52Lamaceta", "53Elarpa", "54Larana"
]

#Definir los colores para el tablero

COLORES_TABLERO = ["#287fe4","#eadb00","#dda8c4"]

@app.route('/loteria')
def loteria_default():
    filas = 4
    columnas = 4
    tablero = []
    for r in range(filas):
        fila_actual = []
        for c in range(columnas):
            color_index = (r + c) % len(COLORES_TABLERO)
            color = COLORES_TABLERO[color_index]
            fila_actual.append({"color": color})
        tablero.append(fila_actual)
    return render_template('tablero.html', filas=filas, columnas=columnas, tablero=tablero)

@app.route('/loteria/<int:x>')
def loteria_filas_dinamicas(x):
    filas = x
    columnas = 4
    tablero = []
    for r in range(filas):
        fila_actual = []
        for c in range(columnas):
            color_index = (r + c) % len(COLORES_TABLERO)
            color = COLORES_TABLERO[color_index]
            fila_actual.append({"color": color})
        tablero.append(fila_actual)
    return render_template('tablero.html', filas=filas, columnas=columnas, tablero=tablero)


if __name__ == "__main__":
    app.run(debug=True)