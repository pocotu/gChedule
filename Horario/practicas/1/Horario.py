import numpy as np

class Agenda:
    def __init__(self, idCurso, idClase, idDocente, idSalon, diaSemana, horario):
        # Inicializa una instancia de Agenda con los identificadores del curso, la clase y el docente
        self.idCurso = idCurso
        self.idClase = idClase
        self.idDocente = idDocente
        self.idSalon =  idSalon
        self.diaSemana = diaSemana
        self.horario = horario

#    def Inicializador_aleatorio(self, salonRango):
#        # Inicializa aleatoriamente las variables de horario dentro de ciertos rangos
#        self.idSalon = np.random.choice([101, 102, 103, 104, 105, 106, 107, 108, 109, 110], 1)[0]  # Genera un numero aleatorio entre 101 y 110 (representando salones)
#        self.diaSemana = np.random.choice([1, 2, 3, 4, 5], 1)[0]  # Genera un numero aleatorio entre 1 y 5 (representando dias de la semana)
#        self.horario = np.random.choice([1, 2, 3, 4, 5], 1)[0]  # Genera un numero aleatorio entre 1 y 6 (representando horarios)

def CostoHorario(poblacion, elite):
    # Calcula el costo (conflicto) de horario para cada horario en la poblacion
    conflictos = []
    n = len(poblacion[0])  # Obtiene el numero de horarios en la poblacion (asume que todos tienen la misma cantidad)

    for p in poblacion:
        conflicto = 0  # Inicializa el contador de conflictos para este horario

        # Compara cada par de horarios para verificar si hay conflictos
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # Compara el id del salon, el dia de la semana y el horario
                if p[i].idSalon == p[j].idSalon and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id de la clase, el dia de la semana y el horario
                if p[i].idClase == p[j].idClase and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id del docente, el dia de la semana y el horario
                if p[i].idDocente == p[j].idDocente and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id de la clase, el id del curso y el dia de la semana
                if p[i].idClase == p[j].idClase and p[i].idCurso == p[j].idCurso and p[i].diaSemana == p[j].diaSemana:
                    conflicto += 1

        conflictos.append(conflicto)  # Agrega el numero de conflictos para este horario a la lista

    # Ordena los horarios en funcion de sus conflictos en orden ascendente
    indice = np.array(conflictos).argsort()

    # Devuelve los indices de los horarios elite (los menos conflictivos) y el numero de conflictos del mejor horario
    return indice[: elite], conflictos[indice[0]]
